# app_c/urls.py
from django.urls import path
from .views import (CommentedComponentsByDaysView, CommentedProductsByDaysView,
                    LatestReportedProductsView, LatestReportedComponentsView,
                    LatestModifiedProductsView, LatestModifiedComponentsView,
                    LatestCommentedComponentsView, LatestCommentedProductsView,
                    ModifiedComponentsByDaysView, ModifiedProductsByDaysView,
                    ReportedComponentsByDaysView, ReportedProductsByDaysView)

urlpatterns = [
    path('latest_reported_products/<int:n>/',
         LatestReportedProductsView.as_view(), name='latest_reported_products'),
    path('latest_reported_components/<int:n>/',
         LatestReportedComponentsView.as_view(), name='latest_reported_components'),
    path('latest_modified_products/<int:n>/',
         LatestModifiedProductsView.as_view(), name='latest_modified_products'),
    path('latest_modified_components/<int:n>/',
         LatestModifiedComponentsView.as_view(), name='latest_modified_components'),
    path('latest_commented_products/<int:n>/',
         LatestCommentedProductsView.as_view(), name='latest_modified_components'),
    path('latest_commented_components/<int:n>/',
         LatestCommentedComponentsView.as_view(), name='latest_modified_components'),
    path('reported_products_by_days/<int:days>/',
         ReportedProductsByDaysView.as_view(), name='reported_products_by_days'),
    path('reported_components_by_days/<int:days>/',
         ReportedComponentsByDaysView.as_view(), name='reported_components_by_days'),
    path('modified_products_by_days/<int:days>/',
         ModifiedProductsByDaysView.as_view(), name='modified_products_by_days'),
    path('modified_components_by_days/<int:days>/',
         ModifiedComponentsByDaysView.as_view(), name='modified_components_by_days'),
    path('commented_products_by_days/<int:days>/',
         CommentedProductsByDaysView.as_view(), name='commented_products_by_days'),
    path('commented_components_by_days/<int:days>/',
         CommentedComponentsByDaysView.as_view(), name='commented_components_by_days'),
]
