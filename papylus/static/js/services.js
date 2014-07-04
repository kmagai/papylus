'use strict';

app.factory('User', [
  '$resource', function($resource) {
    return $resource('/api/user/:id', {}, {
     update: { method: 'PUT', params: { id: '@id' } 
     }
    }
  )
  }
]);

app.factory('List', [
  '$resource', function($resource) {
    return $resource('/api/list/:id', {}, {
     update: { method: 'PUT', params: { id: '@id' } 
     }
    }
  )
  }
]);

app.factory('Item', [
  '$resource', function($resource) {
    return $resource('/api/item/:id', {}, {
      update: { method: 'PUT', params: { id: '@id' }
     }
    }
  )
  }
]);

app.factory('AuthService', function($cookieStore, $location){
  return {
    login: function() {
      window.location.href = 'login/tw';
      // set login cookie like, ('token': 'hogehoge') in controller.py
      // set login cookie like, ('userId': 'kmagai_') in controller.py
    },
    logout: function() {
      $cookieStore.remove('token');
      $cookieStore.remove('userId');
      $location.path('/');
    }
  }
})

