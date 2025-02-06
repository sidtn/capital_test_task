from flask import request, jsonify
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app import db
from string_app.models import StringModel
from string_app.schemas import StringSchema

from string_app import bp


@bp.route("/strings", methods=["POST"])
def create_string():
    try:
        data = request.get_json()
        validated_data = StringSchema(**data)
        new_string = StringModel(value=validated_data.value)
        db.session.add(new_string)
        db.session.commit()
        return jsonify({"id": new_string.id, "value": new_string.value}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500


@bp.route("/strings", methods=["GET"])
def get_strings():
    strings = StringModel.query.all()
    return jsonify([{"id": s.id, "value": s.value} for s in strings])


@bp.route("/strings/<int:id>", methods=["GET"])
def get_string(id):
    string = StringModel.session.get(id)
    if not string:
        return jsonify({"error": "String not found"}), 404
    return jsonify({"id": string.id, "value": string.value})


@bp.route("/strings/<int:id>", methods=["PUT"])
def update_string(id):
    string = StringModel.query.get(id)
    if not string:
        return jsonify({"error": "String not found"}), 404
    try:
        data = request.get_json()
        validated_data = StringSchema(**data)
        string.value = validated_data.value
        db.session.commit()
        return jsonify({"id": string.id, "value": string.value})
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500


@bp.route("/strings/<int:id>", methods=["DELETE"])
def delete_string(id):
    string = StringModel.query.get(id)
    if not string:
        return jsonify({"error": "String not found"}), 404
    db.session.delete(string)
    db.session.commit()
    return jsonify({"message": "String deleted"})


@bp.route("/strings/search", methods=["GET"])
def search_strings():
    keyword = request.args.get("q", "")
    if not keyword:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    strings = StringModel.query.filter(
        StringModel.value.ilike(f"%{keyword}%")
    ).all()
    return jsonify([{"id": s.id, "value": s.value} for s in strings])
