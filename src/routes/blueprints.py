from flask import Blueprint

users_bp = Blueprint("User", __name__)
roles_bp = Blueprint("Role", __name__)
claims_bp = Blueprint("Claim", __name__)
user_claims_bp = Blueprint("UserClaim", __name__)
