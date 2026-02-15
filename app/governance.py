def validate_request(request):
    if "ssn" in request.prompt.lower():
        raise Exception("Potential sensitive data detected")