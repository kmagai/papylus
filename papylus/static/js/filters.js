'use strict';

/* Filters */

/* not used currently, just save it for later use */
angular.module('papylusFilters', []).filter('reverse', function() {
  return function(items) {
    return items.slice().reverse();
  };
});

