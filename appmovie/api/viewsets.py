from appmovie.views import MovieRaitingSerializerAllAll

movierateall_detail = MovieRaitingSerializerAllAll.as_view({
    'get' : 'list',
    'post' : 'create',
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})