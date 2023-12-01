import ormar
from uuid import UUID

from app.models.bills import Bill
from database import BaseMeta


class BankAccount(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bank_accounts"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=128)
    bank_name: str = ormar.String(max_length=128)
    account_type: str = ormar.String(max_length=128)
    agency: str = ormar.String(max_length=128)
    account: str = ormar.String(max_length=128)
    bills: list = ormar.ManyToMany(Bill, related_name='bank_accounts')


class CreditCard(ormar.Model):
    class Meta(BaseMeta):
        tablename = "credit_cards"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=128)
    card_type: str = ormar.String(max_length=128)
    card_number: str = ormar.String(max_length=128)
    expiration_date: str = ormar.String(max_length=128)
    bills: list = ormar.ManyToMany(Bill, related_name='credit_cards')


class Wallet(ormar.Model):
    class Meta(BaseMeta):
        tablename = "wallets"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    name: str = ormar.String(max_length=128)
    public_key: str = ormar.String(max_length=255)
    bills: list = ormar.ManyToMany(Bill, related_name='wallets')

