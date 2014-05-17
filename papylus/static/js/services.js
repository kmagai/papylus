'use strict';

angular.module('listServices', ['ngResource'])
  .factory('List', [
    '$resource', function($resource) {
      return $resource('/api/list/:id', {}, {
       update: { method: 'PUT', params: { id: '@id' } 
       }
      }
    )
    }
    ]);

angular.module('itemServices', ['ngResource'])
  .factory('Item', [
    '$resource', function($resource) {
      return $resource('/amazon/item/:id', {}, {}
      )
    }
  ]);


