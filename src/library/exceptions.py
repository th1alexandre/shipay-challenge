from flask import jsonify


def exception_handler(e):
    if isinstance(e, BaseException):
        return jsonify(error=str(e)), e.status_code
    return jsonify(error="Internal Server Error"), 500


class BaseException(Exception):
    def __init__(self, message, status_code):
        self.status_code = status_code
        super().__init__(message)


class BadRequestException(BaseException):
    def __init__(self, message="Bad Request"):
        super().__init__(message, 400)


class UnauthorizedException(BaseException):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, 401)


class ForbiddenException(BaseException):
    def __init__(self, message="Forbidden"):
        super().__init__(message, 403)


class NotFoundException(BaseException):
    def __init__(self, message="Not Found"):
        super().__init__(message, 404)


class MethodNotAllowedException(BaseException):
    def __init__(self, message="Method Not Allowed"):
        super().__init__(message, 405)


class ConflictException(BaseException):
    def __init__(self, message="Conflict"):
        super().__init__(message, 409)


class PreconditionFailedException(BaseException):
    def __init__(self, message="Precondition Failed"):
        super().__init__(message, 412)


class InternalServerErrorException(BaseException):
    def __init__(self, message="Internal Server Error"):
        super().__init__(message, 500)
