'use strict';

/* Directives */

app.directive('checkUser', ['$rootScope', '$location', '$cookies', 'User', function ($root, $location, $cookies, User) {
  return {
    link: function (scope, elem, attrs, ctrl) {
      $root.$on('$routeChangeStart', function(event, next, current){
        if (!!next.params) {
          var userId = next.params.userId

          User.get({
            id: userId
          }, function(user) {
            if (!hasAccess(user.tw_oauth_token)) {
              event.preventDefault();
              $location.path('/');
            }
          })

          var hasAccess = function(userToken) {
            return next.access.level == 'public' || $cookies.token == userToken ? true: false;
          }
        }
      });
    }
  }
}]);

