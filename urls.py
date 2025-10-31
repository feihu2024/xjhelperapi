from fastapi import FastAPI, Depends
from service.auth import s_login
from router import admin, mall
from router.admin import manage
from router import file, r_schema, r_query, r_update, r_create, r_wx
from router.mall import user


def include_routers(app: FastAPI):
    app.include_router(r_query.router, prefix='/query', tags=['query'])
    app.include_router(r_update.router, prefix='/update', tags=['update'])
    app.include_router(r_create.router, prefix='/create', tags=['create'])
    app.include_router(r_wx.router, prefix='/wx', tags=['wx'])

    # mall user
    app.include_router(mall.user.router, prefix='/mall/user', tags=['/mall/user'])

    # mall admin
    app.include_router(admin.manage.router, prefix='/mall/admin', tags=['/mall/admin'])

    #
    # app.include_router(supplier.user.router, prefix='/supplier/user', tags=['/supplier/user'])
    #
    # app.include_router(flash_good.router, prefix='/mall/package', tags=['/mall/package'])
    # app.include_router(flash_order.router, prefix='/mall/package_order', tags=['/mall/package'])
    #
    # # mall home
    # app.include_router(mall.home.router, prefix='/mall/home', tags=['/mall/home'])
    #
    # # user account
    # app.include_router(mall.account.router, prefix='/mall/account', tags=['/mall/account'])
    #
    # # good collects
    # app.include_router(mall.good.router, prefix='/mall/good', tags=['/mall/good'])
    #
    # # mall order
    # app.include_router(mall.order.router, prefix='/mall/order', tags=['/mall/order'])
    #
    # # user address
    # app.include_router(mall.address.router, prefix='/mall/address', tags=['mall/address'])
    #
    # # mall package
    # # app.include_router(mall.package.router, prefix='/mall/package', tags=['/mall/package'])
    #
    # # mall store
    # app.include_router(mall.store.router, prefix='/mall/store', tags=['/mall/store'])
    #
    # # mall platform
    # app.include_router(mall.platform.router, prefix='/mall/platform', tags=['/mall/platform'])
    #
    #
    #
    # # admin
    # # admin package
    # app.include_router(admin.package.router, prefix='/admin/package', tags=['/admin/package'])
    #
    # # good
    # app.include_router(admin.good.router, prefix='/admin/good', tags=['/admin/good'])
    #
    # # admin package order
    # app.include_router(admin.package_order.router, prefix='/admin/package_order', tags=['/admin/package_order'])
    # app.include_router(admin.good_spec.router, prefix='/admin/good_spec', tags=['/admin/good_spec'])
    #
    # # admin settings
    # app.include_router(admin.settings.router, prefix='/admin/settings', tags=['/admin/settings'])
    #
    # #admin gropsir
    # app.include_router(admin.groupsir.router, prefix='/admin/groupsir', tags=['/admin/groupsir'])
    # app.include_router(admin.balance.router, prefix='/admin/balance', tags=['/admin/balance'])

    # file
    app.include_router(file.router, prefix='/assets', tags=['file'])

    app.include_router(r_schema.router, prefix='/schema', tags=['schema'])
