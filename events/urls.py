from django.urls import path

from .views import (
    EventCategoryListView,
    EventCategoryCreateView,
    EventCategoryUpdateView,
    EventCategoryDeleteView,
    EventCreateView,
    BookEventCreateView,
    ViewBookingsListView,
    EventListView,
    EventUpdateView,
    EventDetailView,
    EventDeleteView,
    AddEventMemberCreateView,
    JoinEventListView,
    RemoveEventMemberDeleteView,
    EventUserWishListView,
    AddEventUserWishListCreateView,
    RemoveEventUserWishDeleteView,
    UpdateEventStatusView,
    CompleteEventList,
    AbsenseUserList,
    CompleteEventUserList,
    CreateUserMark,
    UserMarkList,
    search_event_category,
    search_event,
    create_event,
)

urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    path('create-category/', EventCategoryCreateView.as_view(), name='create-event-category'),
    path('category/<int:pk>/edit/', EventCategoryUpdateView.as_view(), name='edit-event-category'),
    path('category/<int:pk>/delete/', EventCategoryDeleteView.as_view(), name='delete-event-category'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('book-event/', BookEventCreateView.as_view(), name='book-event'),
    path('view-bookings/', ViewBookingsListView.as_view(), name='view-bookings'),
    
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('detail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),
    path('add-event-member/', AddEventMemberCreateView.as_view(), name='add-event-member'),
    path('join-event-list/', JoinEventListView.as_view(), name='join-event-list'),
    path('event-member/<int:pk>/remove/', RemoveEventMemberDeleteView.as_view(), name='remove-event-member'),
    path('event-wish-list/', EventUserWishListView.as_view(), name='event-wish-list'),
    path('add-event-wish-user/', AddEventUserWishListCreateView.as_view(), name='add-event-wish-user'),
    path('event-user-wish/<int:pk>/remove/', RemoveEventUserWishDeleteView.as_view(), name='remove-event-user-wish'),
    path('update-status/<int:pk>/event/', UpdateEventStatusView.as_view(), name='update-event-status'),
    path('complete-event/', CompleteEventList.as_view(), name='complete-event'),
    path('absense-user/', AbsenseUserList.as_view(), name='absense-user'),
    path('complete-event-user/', CompleteEventUserList.as_view(), name='complete-event-user'),
    path('create-user-mark/', CreateUserMark.as_view(), name='create-user-mark'),
    path('user-mark/', UserMarkList.as_view(), name='user-mark'),
    path('search_category/', search_event_category, name='search-event-category'),
    path('search_event/', search_event, name='search-event'),
    path('create/', create_event, name='create'),
]