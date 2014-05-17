'use strict';

angular.module('Papylus', ['papylusServices', 'ngRoute', 'ui.bootstrap'])
  .config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
    $routeProvider
    .when('/list', {
      templateUrl: 'static/partials/post-list.html',
      controller: ListsCtrl
    })
    .when('/list/:id', {
      templateUrl: '/static/partials/post-detail.html',
      controller: ListDetailCtrl
    })
    .when('/user', {
      templateUrl: 'static/partials/post-list.html',
      controller: ListsCtrl
    })
    .when('/add', {
    })
    .otherwise({
      redirectTo: '/'
    })
    ;

    $locationProvider.html5Mode(true);
  }])

