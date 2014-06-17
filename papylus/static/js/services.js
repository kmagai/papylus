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
    return $resource('/api/item/:item_id', {}, {
      update: { method: 'PUT', params: { item_id: '@item_id' } 
     }
    }
  )
  }
]);

app.factory('AuthService', function($cookieStore, $location){
  return {
    login: function() {
      window.location.href = 'login/tw';
    },
    logout: function() {
      $cookieStore.remove('token');
      $location.path('/');
    }
  }
})

