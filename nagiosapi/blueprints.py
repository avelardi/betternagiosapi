from flask import Blueprint, abort, jsonify

from nagiosapi.logic import status_json_or_404

api = Blueprint("api", "api", url_prefix="/api")


@api.route("/")
def all():
    return status_json_or_404()


@api.route("/info/")
@api.route("/info/<field>/")
def info(field=None):
    return status_json_or_404(endpoint="info",
                              field=field)


@api.route("/programstatus/")
@api.route("/programstatus/<field>/")
def programstatus(field=None):
    return status_json_or_404(endpoint="programstatus",
                              field=field)


@api.route("/hoststatus/")
@api.route("/hoststatus/<host_name>/")
@api.route("/hoststatus/<host_name>/<field>/")
def hoststatus(host_name=None, field=None):
    return status_json_or_404(endpoint="hoststatus",
                              host_name=host_name,
                              field=field)


@api.route("/servicestatus/")
@api.route("/servicestatus/<host_name>/")
@api.route("/servicestatus/<host_name>/<service_description>/")
@api.route("/servicestatus/<host_name>/<service_description>/<field>/")
def servicestatus(host_name=None, service_description=None, field=None):
    return status_json_or_404(endpoint="servicestatus",
                              host_name=host_name,
                              service_description=service_description,
                              field=field)


@api.route("/contactstatus/")
@api.route("/contactstatus/<contact_name>/")
@api.route("/contactstatus/<contact_name>/<field>/")
def contactstatus(contact_name=None, field=None):
    return status_json_or_404(endpoint="contactstatus",
                              contact_name=contact_name,
                              field=field)


@api.route("/hostcomment/")
@api.route("/hostcomment/<host_name>/")
@api.route("/hostcomment/<host_name>/<field>/")
def hostcomment(host_name=None, field=None):
    return status_json_or_404(endpoint="hostcomment",
                              host_name=host_name,
                              field=field)
