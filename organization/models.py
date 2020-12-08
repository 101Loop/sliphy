from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from organization.utils import generate_slip_id

user = get_user_model()


class Company(TimeStampedModel):
    """Model to represent Company"""

    user = models.ForeignKey(to=user, on_delete=models.PROTECT)
    company_name = models.CharField(_("Company Name"), max_length=255, blank=False)
    company_mobile = models.CharField(
        _("Company Mobile Number"),
        validators=[RegexValidator(regex=r"^[0][1-9]\d{9}$|^[6-9]\d{9}$")],
        max_length=10,
        unique=True,
        null=True,
        error_messages={
            "unique": _("A Company with that mobile already exists."),
        },
    )
    company_website_url = models.URLField(
        _("Company Website URL"), unique=True, blank=True
    )
    company_address = models.TextField(_("Company Address"))
    company_logo = models.ImageField(
        _("Company Logo"), upload_to="company_logo/", null=True, blank=True
    )
    is_active = models.BooleanField(_("Is Company Active?"), default=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


class Employee(TimeStampedModel):
    """Model to represent Employee"""

    company = models.ForeignKey(to=Company, on_delete=models.PROTECT)
    employee_id = models.CharField(
        _("Employee ID"),
        max_length=255,
        blank=False,
        unique=True,
        error_messages={
            "unique": _("An Employee with that ID already exists."),
        },
    )
    name = models.CharField(_("Employee Full Name"), max_length=255, blank=False)
    email = models.EmailField(
        _("Employee Email"),
        blank=True,
        unique=True,
        error_messages={
            "unique": _("An Employee with that mobile already exists."),
        },
    )
    mobile = models.CharField(
        _("Employee Mobile Number"),
        validators=[RegexValidator(regex=r"^[0][1-9]\d{9}$|^[6-9]\d{9}$")],
        max_length=10,
        unique=True,
        blank=True,
        error_messages={
            "unique": _("An Employee with that mobile already exists."),
        },
    )
    designation = models.CharField(
        _("Employee Designation"), max_length=255, blank=False
    )
    department = models.CharField(_("Employee Department"), max_length=255, blank=False)
    joining_date = models.DateField(_("Employee Joining Date"), blank=True)
    bank_name = models.CharField(_("Employee Bank Name"), blank=True, max_length=255)
    account_holder_name = models.CharField(
        _("Account Holder Name"), blank=True, max_length=255
    )
    account_number = models.CharField(_("Account Number"), blank=True, max_length=255)
    account_type = models.CharField(_("Account Type"), blank=True, max_length=50)
    upi_id = models.CharField(_("UPI ID"), blank=True, unique=True, max_length=50)
    is_active = models.BooleanField(_("Is Employee Active?"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")


class SalarySlip(TimeStampedModel):
    """
    Model to represent SalarySlip

    TODO: Use signals to calculate total earnings
    """

    UPI = "UPI"
    CHEQUE = "CHEQUE"
    NEFT = "NEFT"
    IMPS = "IMPS"
    PAYMENT_METHODS = [
        (UPI, "UPI"),
        (CHEQUE, "CHEQUE"),
        (NEFT, "NEFT"),
        (IMPS, "IMPS"),
    ]
    employee = models.ForeignKey(to=Employee, on_delete=models.PROTECT)
    slip_number = models.CharField(
        _("Salary Slip ID"), max_length=12, default=generate_slip_id
    )
    salary_slip_date = models.DateField(_("Date"), auto_now_add=True)
    # earnings
    basic = models.DecimalField(
        _("Basic & DA"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    house_rent_allowance = models.DecimalField(
        _("House Rent Allowance"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    misc_allowance = models.DecimalField(
        _("Miscellaneous Allowance"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    joining_bonus = models.DecimalField(
        _("Joining Bonus"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    conveyance = models.DecimalField(
        _("Conveyance"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    gross_earnings = models.DecimalField(
        _("Gross Earnings"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    # deductions
    provident_fund = models.DecimalField(
        _("Provident Fund"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    tds_it = models.DecimalField(
        _("TDS/IT"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    professional_tax = models.DecimalField(
        _("Professional Tax"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    gst = models.DecimalField(
        _("GST"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    gross_deductions = models.DecimalField(
        _("Gross Deductions"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    # payments
    net_pay = models.DecimalField(
        _("Net Pay"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    reference_number = models.CharField(_("Transaction ID"), max_length=255, blank=True)
    payment_method = models.CharField(
        _("Payment Method"), choices=PAYMENT_METHODS, default=IMPS, max_length=10
    )
    payment_transfer_date = models.DateField(_("Payment Date"), auto_now_add=True)

    def save(self):
        """
        Calculate Salary
        :return: None
        """
        total_earnings = (
            self.basic
            + self.house_rent_allowance
            + self.misc_allowance
            + self.joining_bonus
            + self.conveyance
        )
        total_deductions = (
            self.provident_fund + self.tds_it + self.professional_tax + self.gst
        )
        net_pay = total_earnings - total_deductions
        self.gross_earnings = total_earnings
        self.gross_deductions = total_deductions
        self.net_pay = net_pay
        super(SalarySlip, self).save()

    def __str__(self):
        return self.slip_number

    class Meta:
        verbose_name = _("Salary Slip")
        verbose_name_plural = _("Salary Slips")
