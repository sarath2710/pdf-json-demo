from pydantic import BaseModel
from typing import List, Optional

# -------------------------
# Shared Sub-sections
# -------------------------

class DocumentHeader(BaseModel):
    authority: Optional[str] = None
    office: Optional[str] = None
    page: Optional[str] = None


class CustomsDeclaration(BaseModel):
    net_weight: Optional[str] = None
    consignee_code: Optional[str] = None
    gross_weight: Optional[str] = None
    intercessor_co: Optional[str] = None
    measurement: Optional[str] = None
    commercial_reg_no: Optional[str] = None
    no_of_packages: Optional[str] = None
    export_to: Optional[str] = None
    marks_numbers: Optional[str] = None
    port_of_loading: Optional[str] = None
    port_of_discharge: Optional[str] = None
    destination: Optional[str] = None
    carrier_name: Optional[str] = None
    voyage_flight_no: Optional[str] = None
    bl_awb_manifest: Optional[str] = None


class GoodsDetails(BaseModel):
    loc: Optional[str] = None
    total_duty: Optional[str] = None
    hs_code: Optional[str] = None
    goods_description: Optional[str] = None
    origin: Optional[str] = None
    foreign_value: Optional[str] = None
    currency_type: Optional[str] = None
    exchange_rate: Optional[str] = None
    cif_local_value: Optional[str] = None
    duty_rate: Optional[str] = None
    income_type: Optional[str] = None
    total_duty_type: Optional[str] = None


class AdditionalGoods(BaseModel):
    hs_code: Optional[str] = None
    description: Optional[str] = None
    origin: Optional[str] = None
    foreign_value: Optional[str] = None
    currency: Optional[str] = None
    exchange_rate: Optional[str] = None
    cif_local_value: Optional[str] = None
    duty_rate: Optional[str] = None
    duty_type: Optional[str] = None
    total_duty: Optional[str] = None


class ExemptionDuty(BaseModel):
    qty: Optional[str] = None
    type: Optional[str] = None
    qty_2: Optional[str] = None
    unit: Optional[str] = None
    net: Optional[str] = None
    gross: Optional[str] = None
    clearing_agent: Optional[str] = None
    license_no: Optional[str] = None
    agency: Optional[str] = None
    release_ref: Optional[str] = None
    sources: Optional[str] = None
    code: Optional[str] = None
    beneficiary: Optional[str] = None


class DutiesAndFees(BaseModel):
    inspection: Optional[str] = None
    inspector: Optional[str] = None
    group_supervisor: Optional[str] = None
    other_remarks: Optional[str] = None
    release_date: Optional[str] = None
    route: Optional[str] = None
    exit_port: Optional[str] = None
    exit_transaction_no: Optional[str] = None
    date: Optional[str] = None
    security_officer: Optional[str] = None
    transit_officer: Optional[str] = None
    total_duty: Optional[str] = None
    handling: Optional[str] = None
    storage: Optional[str] = None
    other_charges: Optional[str] = None
    definite: Optional[str] = None
    total_fee: Optional[str] = None
    payment_method: Optional[str] = None
    guarantee_cheque: Optional[str] = None
    duty: Optional[str] = None
    date_2: Optional[str] = None
    bank: Optional[str] = None
    receipt_no: Optional[str] = None
    bank_2: Optional[str] = None


class FooterNotes(BaseModel):
    distribution: Optional[str] = None


# -------------------------
# Main Models
# -------------------------

class Invoice(BaseModel):
    document_header: Optional[DocumentHeader] = None
    port_type: Optional[str] = None
    dec_type: Optional[str] = None
    dec_date: Optional[str] = None
    dec_no: Optional[str] = None
    customs_declaration: Optional[CustomsDeclaration] = None
    goods_details: Optional[GoodsDetails] = None
    additional_goods: Optional[List[AdditionalGoods]] = None
    exemption_duty: Optional[ExemptionDuty] = None
    duties_and_fees: Optional[DutiesAndFees] = None
    footer_notes: Optional[FooterNotes] = None


class Declaration(BaseModel):
    document_header: Optional[DocumentHeader] = None
    port_type: Optional[str] = None
    dec_type: Optional[str] = None
    dec_date: Optional[str] = None
    dec_no: Optional[str] = None
    customs_declaration: Optional[CustomsDeclaration] = None
    goods_details: Optional[GoodsDetails] = None
    additional_goods: Optional[List[AdditionalGoods]] = None
    exemption_duty: Optional[ExemptionDuty] = None
    duties_and_fees: Optional[DutiesAndFees] = None
    footer_notes: Optional[FooterNotes] = None

# ------------------------------

# from pydantic import BaseModel, Field
# from typing import List, Optional


# # -------------------------
# # Shared Sub-sections
# # -------------------------

# class DocumentHeader(BaseModel):
#     authority: Optional[str]
#     office: Optional[str]
#     page: Optional[str]


# class CustomsDeclaration(BaseModel):
#     net_weight: Optional[str] = Field(alias="5_net_weight")
#     consignee_code: Optional[str] = Field(alias="6_consignee_code")
#     gross_weight: Optional[str] = Field(alias="7_gross_weight")
#     intercessor_co: Optional[str] = Field(alias="8_intercessor_co")
#     measurement: Optional[str] = Field(alias="9_measurement")
#     commercial_reg_no: Optional[str] = Field(alias="10_commercial_reg_no")
#     no_of_packages: Optional[str] = Field(alias="11_no_of_packages")
#     export_to: Optional[str] = Field(alias="12_export_to")
#     marks_numbers: Optional[str] = Field(alias="13_marks_numbers")
#     port_of_loading: Optional[str] = Field(alias="14_port_of_loading")
#     port_of_discharge: Optional[str] = Field(alias="15_port_of_discharge")
#     destination: Optional[str] = Field(alias="16_destination")
#     carrier_name: Optional[str] = Field(alias="17_carrier_name")
#     voyage_flight_no: Optional[str] = Field(alias="18_voyage_flight_no")
#     bl_awb_manifest: Optional[str] = Field(alias="19_bl_awb_manifest")


# class GoodsDetails(BaseModel):
#     loc: Optional[str]
#     total_duty: Optional[str]
#     hs_code: Optional[str]
#     goods_description: Optional[str]
#     origin: Optional[str]
#     foreign_value: Optional[str]
#     currency_type: Optional[str]
#     exchange_rate: Optional[str]
#     cif_local_value: Optional[str]
#     duty_rate: Optional[str]
#     income_type: Optional[str]
#     total_duty_type: Optional[str]


# class AdditionalGoods(BaseModel):
#     hs_code: Optional[str]
#     description: Optional[str]
#     origin: Optional[str]
#     foreign_value: Optional[str]
#     currency: Optional[str]
#     exchange_rate: Optional[str]
#     cif_local_value: Optional[str]
#     duty_rate: Optional[str]
#     duty_type: Optional[str]
#     total_duty: Optional[str]


# class ExemptionDuty(BaseModel):
#     qty: Optional[str]
#     type: Optional[str]
#     qty_2: Optional[str]
#     unit: Optional[str]
#     net: Optional[str]
#     gross: Optional[str]
#     clearing_agent: Optional[str]
#     license_no: Optional[str]
#     agency: Optional[str]
#     release_ref: Optional[str]
#     sources: Optional[str]
#     code: Optional[str]
#     beneficiary: Optional[str]


# class DutiesAndFees(BaseModel):
#     inspection: Optional[str]
#     inspector: Optional[str]
#     group_supervisor: Optional[str]
#     other_remarks: Optional[str]
#     release_date: Optional[str]
#     route: Optional[str]
#     exit_port: Optional[str]
#     exit_transaction_no: Optional[str]
#     date: Optional[str]
#     security_officer: Optional[str]
#     transit_officer: Optional[str]
#     total_duty: Optional[str]
#     handling: Optional[str]
#     storage: Optional[str]
#     other_charges: Optional[str]
#     definite: Optional[str]
#     total_fee: Optional[str]
#     payment_method: Optional[str]
#     guarantee_cheque: Optional[str]
#     duty: Optional[str]
#     date_2: Optional[str]
#     bank: Optional[str]
#     receipt_no: Optional[str]
#     bank_2: Optional[str]


# class FooterNotes(BaseModel):
#     distribution: Optional[str]


# # -------------------------
# # Main Models
# # -------------------------

# class Invoice(BaseModel):
#     document_header: Optional[DocumentHeader]
#     port_type: Optional[str]
#     dec_type: Optional[str]
#     dec_date: Optional[str]
#     dec_no: Optional[str]
#     customs_declaration: Optional[CustomsDeclaration]
#     goods_details: Optional[GoodsDetails]
#     additional_goods: Optional[List[AdditionalGoods]]
#     exemption_duty: Optional[ExemptionDuty]
#     duties_and_fees: Optional[DutiesAndFees]
#     footer_notes: Optional[FooterNotes]


# class Declaration(BaseModel):
#     document_header: Optional[DocumentHeader]
#     port_type: Optional[str] = Field(alias="1_port_type")
#     dec_type: Optional[str] = Field(alias="2_dec_type")
#     dec_date: Optional[str] = Field(alias="3_dec_date")
#     dec_no: Optional[str] = Field(alias="4_dec_no")
#     customs_declaration: Optional[CustomsDeclaration]
#     goods_details: Optional[GoodsDetails]
#     additional_goods: Optional[List[AdditionalGoods]]
#     exemption_duty: Optional[ExemptionDuty]
#     duties_and_fees: Optional[DutiesAndFees]
#     footer_notes: Optional[FooterNotes]
