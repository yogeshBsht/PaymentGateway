import base64
from datetime import datetime
import os
from app import db


class Payment(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    
    card_type           = db.Column(db.String(32))
    number              = db.Column(db.Integer)
    expiration_month    = db.Column(db.Integer)
    expiration_year     = db.Column(db.Integer)
    cvv                 = db.Column(db.Integer)
    
    amount              = db.Column(db.Integer)
    currency            = db.Column(db.String(32))
    
    status              = db.Column(db.String(32))
    authorization_code  = db.Column(db.String(32))
    time                = db.Column(db.DateTime)
    
    def from_dict(self, data):
        for field in ['amount', 'currency', 'card_type']:
            setattr(self, field, data[field])
        
        for field in ['number', 'expiration_year',\
                        'expiration_month', 'cvv']:
            setattr(self, field, data['card'][field])
        
        if self.check_payment(data) and self.check_card(data):
            setattr(self, 'status', 'success')
        else:
            setattr(self, 'status', 'failure')

        self.set_authorization_code()
        setattr(self, 'time', datetime.utcnow())  

    def to_dict(self):
        data = {
            'amount': self.amount,
            'currency': self.currency,            
            'type': self.card_type,
            'card':{
                    'number': self.number,
                    },
            'status': self.status,
            'authorization_code': self.authorization_code,
            'time': self.time.strftime("%Y-%m-%d %H:%M:%S")
            }
        return data

    def check_payment(self, data):
        return int(data['amount'])>0 \
                and data['card_type'] in ['credit-card', 'debit-card']

    def check_card(self, data):
        now  = datetime.utcnow()
        return datetime(int(data['card']['expiration_year']), int(data['card']['expiration_month']), 28) > now \
                and data['card']['cvv'].isdigit() and len(data['card']['number']) == 12

    def set_authorization_code(self):
        self.authorization_code = base64.b64encode(os.urandom(24)).decode('utf-8')