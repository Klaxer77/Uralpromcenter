from sqladmin import ModelView 
from app.users.models import Users  #noqa
from app.products.categories.models import Categories  #noqa
from app.products.models import Products  #noqa
from app.news.models import News  #noqa
from app.recall.models import Recall  #noqa
from app.progress.models import Progress  #noqa
from app.email.send_request.models import SendRequest  #noqa
from app.email.order_call.models import OrderCall  #noqa


#Нельзя автоматизировать процесс добавления картинки в хранилище S3


class SendRequestAdmin(ModelView, model=SendRequest):
    column_list = [c.name for c in SendRequest.__table__.c]
    can_delete = False
    can_edit = False
    can_create = False
    name = "Заявка"
    name_plural = "Заявки"
    icon = "fa-solid fa-code-pull-request"
    
class OrderCallAdmin(ModelView, model=OrderCall):
    column_list = [c.name for c in OrderCall.__table__.c]
    can_delete = False
    can_edit = False
    can_create = False
    name = "Заказ звонка"
    name_plural = "Заказы на звонки"
    icon = "fa-solid fa-phone"

class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    
class RecallAdmin(ModelView, model=Recall):
    column_list = [c.name for c in Recall.__table__.c]
    name = "Отзыв"
    name_plural = "Отзывы"
    icon = "fa-solid fa-star"
    
class ProgressAdmin(ModelView, model=Progress):
    column_list = [c.name for c in Progress.__table__.c]
    name = "Достижение"
    name_plural = "Достижения"
    icon = "fa-solid fa-bars-progress"


class CategoriesAdmin(ModelView, model=Categories):
    column_list = [c.name for c in Categories.__table__.c] + [Categories.products, Categories.parent_category]
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-layer-group"


class ProductsAdmin(ModelView, model=Products):
    column_list = [c.name for c in Products.__table__.c] + [Products.subcategories]
    name = "Продукт"
    name_plural = "Продукты"
    icon = "fa-brands fa-product-hunt"


class NewsAdmin(ModelView, model=News):
    column_list = [c.name for c in News.__table__.c]
    name = "Новость"
    name_plural = "Новости"
    icon = "fa-solid fa-newspaper"
