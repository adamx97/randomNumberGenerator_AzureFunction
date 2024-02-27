import azure.functions as func
import logging
import json
import rd_functions_p


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="rand16ints", auth_level=func.AuthLevel.ANONYMOUS)
def rand16ints(req: func.HttpRequest) -> func.HttpResponse:

    count = (
        int(req.params.get("count"))
        if (req.params.get("count") and int(req.params.get("count")) > 0)
        else 1
    )  # default is 1
    if req.params.get("output"):
        output = (
            str.upper(req.params.get("output"))
            if ((str.upper(req.params.get("output"))) in ["JSON", "STRING"])
            else "STRING"
        )  # default is JSON
    else:
        output = "STRING"

    logging.info(
        "rand16ints (output: {0}, count: {1}): Python HTTP trigger function processed a request.".format(
            output, count
        )
    )
    rdf = rd_functions_p.RdFunctions()
    a = list()
    for _ in range(count):
        a.append((str)(rdf.RdRand16_Retry()))
    if output == "STRING":
        return func.HttpResponse(
            "Accepted querystring parameters: count (int) and/or output (STRING|JSON).<br />"
            + f"{count} unsigned 16 bit integer(s), output: {output}:  <br />Random number(s):<br />{', '.join(a)}",
            mimetype="text/html",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps(a),
            mimetype="application/json",
            status_code=200,
        )


@app.route(route="rand32ints", auth_level=func.AuthLevel.ANONYMOUS)
def rand32ints(req: func.HttpRequest) -> func.HttpResponse:
    count = (
        int(req.params.get("count"))
        if (req.params.get("count") and int(req.params.get("count")) > 0)
        else 1
    )  # default is 1
    if req.params.get("output"):
        output = (
            str.upper(req.params.get("output"))
            if ((str.upper(req.params.get("output"))) in ["JSON", "STRING"])
            else "STRING"
        )  # default is JSON
    else:
        output = "STRING"

    logging.info(
        "rand32ints (output: {0}, count: {1}): Python HTTP trigger function processed a request.".format(
            output, count
        )
    )
    rdf = rd_functions_p.RdFunctions()
    a = list()
    for _ in range(count):
        a.append((str)(rdf.RdRand32_Retry()))
    if output == "STRING":
        return func.HttpResponse(
            "Accepted querystring parameters: count (int) and/or output (STRING|JSON).<br />"
            + f"{count} unsigned 32 bit integer(s), output: {output}:  <br />Random number(s):<br />{', '.join(a)}",
            mimetype="text/html",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps(a),
            mimetype="application/json",
            status_code=200,
        )


@app.route(route="rand64ints", auth_level=func.AuthLevel.ANONYMOUS)
def rand64ints(req: func.HttpRequest) -> func.HttpResponse:
    count = (
        int(req.params.get("count"))
        if (req.params.get("count") and int(req.params.get("count")) > 0)
        else 1
    )  # default is 1
    if req.params.get("output"):
        output = (
            str.upper(req.params.get("output"))
            if ((str.upper(req.params.get("output"))) in ["JSON", "STRING"])
            else "STRING"
        )  # default is JSON
    else:
        output = "STRING"

    logging.info(
        "rand64ints (output: {0}, count: {1}): Python HTTP trigger function processed a request.".format(
            output, count
        )
    )
    rdf = rd_functions_p.RdFunctions()
    a = list()
    for _ in range(count):
        a.append((str)(rdf.RdRand64_Retry()))
    if output == "STRING":
        return func.HttpResponse(
            "Accepted querystring parameters: count (int) and/or output (STRING|JSON).<br />"
            + f"{count} unsigned 64 bit integer(s), output: {output}:  <br />Random number(s):<br />{', '.join(a)}",
            mimetype="text/html",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps(a),
            mimetype="application/json",
            status_code=200,
        )


@app.route(route="randuints", auth_level=func.AuthLevel.ANONYMOUS)
def randuints(req: func.HttpRequest) -> func.HttpResponse:
    count = (
        int(req.params.get("count"))
        if (req.params.get("count") and int(req.params.get("count")) > 0)
        else 1
    )  # default is 1
    if req.params.get("output"):
        output = (
            str.upper(req.params.get("output"))
            if ((str.upper(req.params.get("output"))) in ["JSON", "STRING"])
            else "STRING"
        )  # default is JSON
    else:
        output = "STRING"

    logging.info(
        "randuints (output: {0}, count: {1}): Python HTTP trigger function processed a request.".format(
            output, count
        )
    )
    rdf = rd_functions_p.RdFunctions()
    uintArray = rdf.RdRand_Get_N_Uints(count)
    pyArray = [str(a) for a in uintArray]
    if output == "STRING":
        return func.HttpResponse(
            "Accepted querystring parameters: count (int) and/or output (STRING|JSON).<br />"
            + f"{count} unsigned integer(s), output: {output}:  <br />Random number(s):<br />{', '.join(pyArray)}",
            mimetype="text/html",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps(pyArray),
            mimetype="application/json",
            status_code=200,
        )


@app.route(route="randbytes", auth_level=func.AuthLevel.ANONYMOUS)
def randbytes(req: func.HttpRequest) -> func.HttpResponse:
    count = (
        int(req.params.get("count"))
        if (req.params.get("count") and int(req.params.get("count")) > 0)
        else 1
    )  # default is 1
    if req.params.get("output"):
        output = (
            str.upper(req.params.get("output"))
            if ((str.upper(req.params.get("output"))) in ["JSON", "STRING"])
            else "STRING"
        )  # default is JSON
    else:
        output = "STRING"

    logging.info(
        "randbytes (output: {0}, count: {1}): Python HTTP trigger function processed a request.".format(
            output, count
        )
    )
    rdf = rd_functions_p.RdFunctions()
    byteArray = rdf.RdRand_Get_Bytes(count)
    pyArray = [f"{a:0>2X}" for a in byteArray]
    if output == "STRING":
        return func.HttpResponse(
            "Accepted querystring parameters: count (int) and/or output (STRING|JSON).<br />"
            + f"{count} byte(s), output: {output}:  <br />Byte(s):<br />{' '.join(pyArray)}",
            mimetype="text/html",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps(pyArray),
            mimetype="application/json",
            status_code=200,
        )
