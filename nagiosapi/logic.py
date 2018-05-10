import os

from flask import abort, jsonify

NAGIOS_STATUS_PATH = os.getenv("NAGIOS_STATUS_PATH",
                               default="/usr/local/nagios/var/status.dat")


def object_list_from_status_dat(path=NAGIOS_STATUS_PATH):
    skip_characters = "\n", "#"  # skip comments and empty lines

    objects = []

    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        current = len(objects) - 1

        if line[0] in skip_characters:
            continue

        if "{" in line:  # the start of a block includes an open brace
            name = line[:-2].strip()  # the string before the curly
            objects.append({})
            continue

        elif "}" in line:  # the end of a block - so, this object is complete
            objects[current] = {name: objects[current]}
            continue

        else:  # must be a property within a block
            key = line.split("=")[0].strip()
            value = "".join(line.replace(f"{key}=", "")).strip()
            objects[current][key] = value
            continue

    return objects


def status_json_or_404(endpoint=None, field=None, **kwargs):
    filters = {k: v for k, v in kwargs.items() if v is not None}

    objects = object_list_from_status_dat(path=NAGIOS_STATUS_PATH)

    if endpoint:
        objects = list(
            filter(lambda o: endpoint in o, objects)
        )

        if filters:
            objects = list(
                filter(lambda o: k in o[endpoint] and o[endpoint][k] == v,
                       objects)
                for k, v in filters.items()
            )

        if field:
            objects = list(
                map(lambda o: o[endpoint][field], objects)
            )

    if not objects:
        abort(404)

    if len(objects) == 1:
        objects = objects[0]

    return jsonify(objects)
