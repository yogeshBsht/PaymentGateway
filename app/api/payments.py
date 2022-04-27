from flask import jsonify, request, url_for
from app import db
from app.models import Payment
from app.api import bp
from app.api.errors import bad_request


@bp.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    return jsonify(Payment.query.get_or_404(id).to_dict())


@bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json() or {}
    for field in ['card_type','card', 'amount', 'currency']:
        if field not in data:
            return bad_request(f'Payment request must include {field}')
    payment = Payment()
    payment.from_dict(data)
    db.session.add(payment)
    db.session.commit()
    response = jsonify(payment.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_payment', id=payment.id)
    return response