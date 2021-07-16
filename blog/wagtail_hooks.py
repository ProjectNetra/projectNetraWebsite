from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from blog.models import BlogCategory, BlogPage, Project, FooterLink


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_label = 'ProjectNetra Projects'
    exclude_from_explorer = True

    # add_to_settings_menu = True


class CategoryAdmin(ModelAdmin):
    model = BlogCategory
    menu_label = 'ProjectNetra Categories'
    exclude_from_explorer = True


class BlogAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'ProjectNetra Blogs'


class FooterLinkAdmin(ModelAdmin):
    model = FooterLink
    menu_label = 'ProjectNetra links'
    exclude_from_explorer = True
    
class ProjectNetraAdminGroup(ModelAdminGroup):
    menu_label = 'ProjectNetra'
    menu_icon = 'snippet'
    menu_order = 100
    items = (ProjectAdmin, CategoryAdmin, BlogAdmin,FooterLinkAdmin)



modeladmin_register(ProjectNetraAdminGroup)
