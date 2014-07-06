'use strict';

/* Directives */

app.directive('checkUser', ['$rootScope', '$location', '$cookies', '$http', 'User', function ($root, $location, $cookies, $http, User) {
  return {
    link: function (scope, elem, attrs, ctrl) {
      $root.$on('$routeChangeStart', function(event, current, next){
        if (!!current.params) {
          var userId = current.params.userId
          User.get({
            id: userId
          }, function(user) {
            $http({
              method: 'POST',
              url: '/get_hashed_oauth',
              data: 'oauth_token=' + user.tw_oauth_token,
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            })
              .success(function(data, status, headers, config) {
                if (!hasAccess(data)) {
                  event.preventDefault();
                  $location.path('/');
                }
              })
              .error(function(data, status, headers, config) {
                console.log(data);
                console.log(status);
                console.log(headers);
                console.log(config);
              });
          }, function(err) {
            // No user for the path
            $location.path('/');
          }
          )

          var hasAccess = function(userToken) {
            userToken = JSON.parse(userToken);
            return current.access.level == 'public' || $cookies.token == userToken ? true: false;
          }
        }
      });
    }
  }
}]);

app.directive('focusMe', ['$timeout', function ($timeout) {
  return {
    link: function (scope, elem, attrs) {
      scope.$watch(attrs.focusMe, function(value) {
        if(value === true) { 
          $timeout(function() {
            element[0].focus();
          }, 20);
        }
      });
    }
  }
}])
