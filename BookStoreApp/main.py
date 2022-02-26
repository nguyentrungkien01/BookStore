from BookStoreApp import app, init_tables, init_admin

if __name__ == '__main__':
    init_tables()
    init_admin()
    app.run()
