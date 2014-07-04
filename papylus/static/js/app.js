'use strict';

var app = angular.module('Papylus', ['ngRoute', 'ngResource', 'ui.bootstrap', 'ngCookies'])
.config(function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: '/static/partials/landing.html',
      access: {
        level: 'public'
      }
    })
    .when('/login/tw', {
      redirectTo: '/login/tw',
      access: {
        level: 'public'
      }
    })
    .when('/list/:userId/:listId', {
      templateUrl: '/static/partials/list.html',
      controller: 'ListCtrl',
      access: {
        level: 'public'
      }
    })
    .when('/edit/:userId/:listId', {
      templateUrl: '/static/partials/list-edit.html',
      controller: 'ListEditCtrl',
      access: {
        level: 'user'
      }
    })
    .when('/user/:userId', {
      templateUrl: 'static/partials/user.html',
      controller: 'UserCtrl',
      access: {
        level: 'user'
      }
    })
    .otherwise({
      redirectTo: '/'
    });

  $locationProvider.html5Mode(true);
})

