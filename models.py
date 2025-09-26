from pydantic import BaseModel
from typing import List, Optional


# -------------------------
# Shared Sub-sections
# -------------------------

class DocumentHeader(BaseModel):
    authority: Optional[str]
    office: Optional[str]
    page: Optional[str]


class CustomsDeclaration(BaseModel):
    net_weight: Optional[str]
    consignee_code: Optional[str]
    gross_weight: Optional[str]
    intercessor_co: Optional[str]
    measurement: Optional[str]
    commercial_reg_no: Optional[str]
    no_of_packages: Optional[str]
    export_to: Optional[str]
    marks_numbers: Optional[str]
    port_of_loading: Optional[str]
    port_of_discharge: Optional[str]
    destination: Optional[str]
    carrier_name: Optional[str]
    voyage_flight_no: Optional[str]
    bl_awb_manifest: Optional[str]


class GoodsDetails(BaseModel):
    loc: Optional[str]
    total_duty: Optional[str]
    hs_code: Optional[str]
    goods_description: Optional[str]
    origin: Optional[str]
    foreign_value: Optional[str]
    currency_type: Optional[str]
    exchange_rate: Optional[str]
    cif_local_value: Optional[str]
    duty_rate: Optional[str]
    income_type: Optional[str]
    total_duty_type: Optional[str]


class AdditionalGoods(BaseModel):
    hs_code: Optional[str]
    description: Optional[str]
    origin: Optional[str]
    foreign_value: Optional[str]
    currency: Optional[str]
    exchange_rate: Optional[str]
    cif_local_value: Optional[str]
    duty_rate: Optional[str]
    duty_type: Optional[str]
    total_duty: Optional[str]


class ExemptionDuty(BaseModel):
    qty: Optional[str]
    type: Optional[str]
    qty_2: Optional[str]
    unit: Optional[str]
    net: Optional[str]
    gross: Optional[str]
    clearing_agent: Optional[str]
    license_no: Optional[str]
    agency: Optional[str]
    release_ref: Optional[str]
    sources: Optional[str]
    code: Optional[str]
    beneficiary: Optional[str]


class DutiesAndFees(BaseModel):
    inspection: Optional[str]
    inspector: Optional[str]
    group_supervisor: Optional[str]
    other_remarks: Optional[str]
    release_date: Optional[str]
    route: Optional[str]
    exit_port: Optional[str]
    exit_transaction_no: Optional[str]
    date: Optional[str]
    security_officer: Optional[str]
    transit_officer: Optional[str]
    total_duty: Optional[str]
    handling: Optional[str]
    storage: Optional[str]
    other_charges: Optional[str]
    definite: Optional[str]
    total_fee: Optional[str]
    payment_method: Optional[str]
    guarantee_cheque: Optional[str]
    duty: Optional[str]
    date_2: Optional[str]
    bank: Optional[str]
    receipt_no: Optional[str]
    bank_2: Optional[str]


class FooterNotes(BaseModel):
    distribution: Optional[str]


# -------------------------
# Main Models
# -------------------------

class Invoice(BaseModel):
    document_header: Optional[DocumentHeader]
    port_type: Optional[str]
    dec_type: Optional[str]
    dec_date: Optional[str]
    dec_no: Optional[str]
    customs_declaration: Optional[CustomsDeclaration]
    goods_details: Optional[GoodsDetails]
    additional_goods: Optional[List[AdditionalGoods]]
    exemption_duty: Optional[ExemptionDuty]
    duties_and_fees: Optional[DutiesAndFees]
    footer_notes: Optional[FooterNotes]


class Declaration(BaseModel):
    document_header: Optional[DocumentHeader]
    port_type: Optional[str]
    dec_type: Optional[str]
    dec_date: Optional[str]
    dec_no: Optional[str]
    customs_declaration: Optional[CustomsDeclaration]
    goods_details: Optional[GoodsDetails]
    additional_goods: Optional[List[AdditionalGoods]]
    exemption_duty: Optional[ExemptionDuty]
    duties_and_fees: Optional[DutiesAndFees]
    footer_notes: Optional[FooterNotes]
