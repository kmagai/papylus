'use strict';

/* Controllers */

function ListsCtrl($scope, $modal, $log, List) {

  List.get({}, function(lists) {
    $scope.lists = lists.objects;

    $scope.delete_list = function(index) {
      var isConfirmed = confirm('このリストを削除しますか？');
      if (isConfirmed) {
        // index is reversed
        var index = $scope.lists.length - index -1
        var targetlist = $scope.lists[index];

        List.delete({ id: targetlist.id },
          function(list) {
            $scope.lists.splice(index, 1);
          }
        )
      }
    }

    // Modal
    $scope.modal = function() {
      var modalInstance = $modal.open({
        templateUrl: 'newListModal.html',
        controller: newListModalCtrl,
        resolve: {
          lists: function() {
            return $scope.lists
          }
        }
      })
      modalInstance.result.then(function (list) {
        $scope.lists.push(list);
      }, function () {
        $log.info('Modal dismissed at: ' + new Date());
      });
    }

  });
};

function newListModalCtrl($scope, $modalInstance, List, lists) {

  $scope.list = {'title':'', 'body':''}

  $scope.addList = function() {
    var newList = {
      title: $scope.list.title,
      body: $scope.list.body
    };

    List.save({}, {
      title: $scope.list.title,
      body: $scope.list.body
    }, function(list) {
      $modalInstance.close(list);
    }
    )
  }

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };

}

function ListDetailCtrl($scope, $routeParams,$modal, $location, List) {
  var postQuery = List.get({
    id: $routeParams.id
  }, function(list) {
    $scope.list = list;
    $scope.items = [];

    $scope.searchItemModal = function() {
      var modalInstance = $modal.open({
        templateUrl: 'searchItemModal.html',
        controller: searchItemModalCtrl,
      })

      modalInstance.result.then(function (list) {
        $scope.items.push(list)
      }, function () {
        $log.info('Modal dismissed at: ' + new Date());
      });
    }

    $scope.reviseList = function() {

      List.update({
        id: $routeParams.id
      }, {
        title: $scope.list.title,
        body: $scope.list.body
      }, function(list) {
        $location.path( "/user" );
      }
      )
    }

    $scope.cancel = function() {
      $location.path( "/user" );
    }

  });
}

function searchItemModalCtrl($scope, $modalInstance, Item) {

  $scope.data = {'query':''}
  $scope.searchAmazon = function() {
    $http({method: 'GET', url: '/search/item'}).
      success(function(data, status, headers, config) {
        console.log(data)
        console.log(status)
        console.log(headers)
        console.log(config)
      }).
      error(function(data, status, headers, config) {
        console.log(data)
        console.log(status)
        console.log(headers)
        console.log(config)
      });
  }

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };

}
