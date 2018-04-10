from flask import abort, jsonify
import socket


NAGIOS_STATUS_PATH = "/usr/local/nagios/var/status.dat" if "nagios" in socket.gethostname() else "/Users/mcintosh/status.dat"


def status_json_or_404(endpoint=None, field=None, **filters):
    filters = {k: v for k, v in filters.items() if v is not None}

    skip_chars = "\n", "#"  # skip comments and empty lines

    object_list = []

    with open(NAGIOS_STATUS_PATH, "r") as f:
        lines = f.readlines()

    for line in lines:
        current = len(object_list) - 1

        if line[0] in skip_chars:
            continue

        if "{" in line:  # the start of a block includes an open brace
            object_name = line[:-2].strip()  # the string before the curly
            object_list.append({})
            continue

        elif "}" in line:  # the end of a block - so, this object is complete
            object_list[current] = {object_name: object_list[current]}
            continue

        else:  # must be a property within a block
            key = line.split("=")[0].strip()
            value = "".join(line.replace(f"{key}=", "")).strip()
            object_list[current][key] = value
            continue

    if endpoint:  # an `endpoint` is a block in the status.dat file
        object_list = list(filter(lambda o: endpoint in o, object_list))

        if filters:  # filter based on any keyword argumments that are passed in
            for k, v in filters.items():
                object_list = list(filter(lambda o: k in o[endpoint] and o[endpoint][k] == v, object_list))

        if field:  # if a field is specified, return that field's value
            object_list = list(map(lambda o: o[endpoint][field], object_list))

    if not object_list:
        abort(404)

    return jsonify(object_list[0]) if len(object_list) == 1 else jsonify(object_list)
