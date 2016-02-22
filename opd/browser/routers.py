class OpdRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.object_name in ['Gtin_img','Brand_img','Owner_img']:
            return 'images'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.object_name in ['Gtin_img','Brand_img','Owner_img']:
            return 'images'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'imgdb'
        database.
        """
        return None
