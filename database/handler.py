from .models import *


def add_email(email):
    """
    Add email to the database.

    :param email: str
    :return: bool
    """
    try:
        if not Email.objects.filter(email=email).exists():
            Email.objects.create(
                email=email
            )
        return True
    except BaseException as e:
        return False


def add_hack(hack_dict):
    """
    Add hack to the database.

    :param hack_dict: dict
    :return: bool
    """
    try:
        for hack in hack_dict:
            hack_site = hack['Domain']
            hack_description = hack['Description']
            hack_title = hack['Name']
            hack_pwn_count = hack['PwnCount']
            if not Hacks.objects.filter(
                site=hack_site,
                description=hack_description,
                title=hack_title,
                pwn_count=hack_pwn_count
            ).exists():
                Hacks.objects.create(
                    site=hack_site,
                    description=hack_description,
                    title=hack_title,
                    pwn_count=hack_pwn_count
                )
        return True
    except BaseException:
        return False


def map_email_hacks(email, hack_dict):
    try:
        email_obj = Email.objects.filter(email=email).first()
        for hack in hack_dict:
            hack_site = hack['Domain']
            hack_description = hack['Description']
            hack_title = hack['Name']
            hack_pwn_count = hack['PwnCount']
            hack_obj = Hacks.objects.filter(
                site=hack_site,
                description=hack_description,
                title=hack_title,
                pwn_count=hack_pwn_count
            ).first()
            HackMap.objects.create(
                email=email_obj,
                hack=hack_obj
            )
        return True
    except BaseException:
        return False
