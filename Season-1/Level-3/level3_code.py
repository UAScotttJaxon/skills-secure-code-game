# Renamed from code.py for import clarity


import os

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            return None

        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "assets")
        abs_assets_dir = os.path.abspath(assets_dir)
        prof_picture_path = os.path.abspath(os.path.normpath(os.path.join(assets_dir, path)))

        # Prevent path traversal: ensure the resolved path is within the assets directory
        if not prof_picture_path.startswith(abs_assets_dir + os.sep):
            return None

        try:
            with open(prof_picture_path, 'rb') as pic:
                picture = bytearray(pic.read())
        except Exception:
            return None

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "assets")
        abs_assets_dir = os.path.abspath(assets_dir)
        abs_path = os.path.abspath(os.path.normpath(path))

        # Prevent path traversal: ensure the resolved path is within the assets directory
        if not abs_path.startswith(abs_assets_dir + os.sep):
            return None

        try:
            with open(abs_path, 'rb') as form:
                tax_data = bytearray(form.read())
        except Exception:
            return None

        # assume that tax data is returned on screen after this
        return abs_path
