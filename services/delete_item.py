from repository.sqlite_db import Database


def delete_item(id):
    items = Database("Ollivanders.sqlite")
    #sql = f"delete from Item where name='{name}' and sell_in='{sell_in}' and quality='{quality}'"
    sql = f"delete from Item where id = '{id}'"
    items.execute(sql)
    items.commit()
    items.close()
