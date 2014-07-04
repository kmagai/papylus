'use strict';

/* Controllers */

var RootCtrl = function ($scope, $timeout, AuthService, $cookies, User) {
  if ($cookies.userId) {
    User.get({
      id: $cookies.userId
    }, function(user) {
      $scope.user = user;
    }
    )
  } else {
    $scope.user = null;
  }

  $scope.logout = function() {
    AuthService.logout()
    $scope.user = null;
  }
  $scope.login = function() {
    AuthService.login()
  }
}

var UserCtrl = function ($scope, $modal, $log, $location, $cookies, $routeParams, AuthService, List, User) {

  User.get({
    id: $cookies.userId
  }, function(user) {
    $scope.user = user;

    if ($scope.user.associates_id == 'papylus-22') {
      $scope.user.associates_id = '';
    }
    $scope.user.edit = false;

    $scope.editUser = function() {
      $scope.user.edit = true;
    }

    $scope.editDone = function() {
      $scope.user.edit = false;

      if ($scope.user.associates_id == ''){
        $scope.user.associates_id = 'papylus-22'
      }

      User.update({
        id: $routeParams.userId
      }, {
        name: $scope.user.name,
        description: $scope.user.description,
        associates_id: $scope.user.associates_id
      }, function(user) {
        $scope.user = user;
        if (user.associates_id == 'papylus-22') {
          $scope.user.associates_id = '';
        }
        $scope.user.edit = false;
      }
      )
    }

    $scope.delete_list = function(index) {
      var isConfirmed = confirm('このリストを削除しますか？');
      if (isConfirmed) {
        // index is reversed
        var index = $scope.user.lists.length - index -1
        var targetlist = $scope.user.lists[index];
    
        List.delete({ id: targetlist.id },
          function(list) {
            $scope.user.lists.splice(index, 1);
          }
        )
      }
    }
    
    $scope.add_list = function() {
      List.save({}, {
        title: $scope.list.title,
        user_id: $routeParams.userId
      }, function(list) {
        $scope.user.lists.push(list);
        $scope.list.title = '';
      }
      )
    }

  }
  )

};


var ListEditCtrl = function ($scope, $routeParams, $modal, $location, $log, List, Item) {
  List.get({
    id: $routeParams.listId
  }, function(list) {
    $scope.list = list;

    $scope.delete_item = function(index) {
      var isConfirmed = confirm('このリストを削除しますか？');
      if (isConfirmed) {
        var targetitem = $scope.list.items[index];
        Item.delete({ id: targetitem.id },
          function(item) {
            $scope.list.items.splice(index, 1);
          }
        )
      }
    }
    
    $scope.searchItemModal = function() {
      var modalInstance = $modal.open({
        templateUrl: 'searchItemModal.html',
        controller: searchItemModalCtrl,
        resolve: {
          list: function() {
            return $scope.list
          }
        }
      })

      modalInstance.result.then(function (item) {
        $scope.list.items.push(item)
      }, function () {
        $log.info('Modal dismissed at: ' + new Date());
      });
    }

    $scope.reviseList = function() {
      List.update({
        id: $routeParams.listId
      }, {
        title: $scope.list.title,
        items: $scope.list.items
      }, function(list) {
        $location.path("/user/" + $scope.list.user_id);
      }
      )
    }

    $scope.cancel = function() {
      $location.path("/user/" + $scope.list.user_id);
    }

  });
}

var searchItemModalCtrl = function($scope, $modalInstance, $http, list, Item) {

  $scope.data = {'query':''}
  $scope.searchItem = function() {
    $http.get('/search/item?q=' + $scope.data.query).
      success(function(data, status, headers, config) {
        $scope.items = data
      }).
      error(function(data, status, headers, config) {
        console.log(status)
      });
  }

  $scope.addItem = function(index) {
    var item = $scope.items.splice(index, 1);
    Item.save({}, {
      name: item[0].name,
      url: item[0].url,
      img: item[0].img,
      publisher: item[0].publisher,
      pub_date: item[0].pub_date,
      list_id: list.id
    }, function(item) {
      $modalInstance.close(item);
    }, function(response) {
      console.log(response)
      $modalInstance.dismiss('cancel');
    }
    )
  }

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
}

var ListCtrl = function ($scope, $routeParams, $modal, $location, $log, List, Item) {
  var postQuery = List.get({
    id: $routeParams.listId
  }, function(list) {
    $scope.list = list;
    $scope.searchItemModal = function() {
      var modalInstance = $modal.open({
        templateUrl: 'searchItemModal.html',
        controller: searchItemModalCtrl,
        resolve: {
          list: function() {
            return $scope.list
          }
        }
      })

      modalInstance.result.then(function (item) {
        $scope.list.items.push(item)
      }, function () {
        $log.info('Modal dismissed at: ' + new Date());
      });
    }

    $scope.reviseList = function() {
      List.update({
        id: $routeParams.listId
      }, {
        title: $scope.list.title,
      }, function(list) {
        $location.path( "/user/" + $scope.list.user_id );
      }
      )
    }

    $scope.cancel = function() {
      $location.path("/user/" + $scope.list.user_id);
    }

  });
}
