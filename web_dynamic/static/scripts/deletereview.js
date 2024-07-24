// function to delete review
function deleteReview(reviewId, userId) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/reviews/${reviewId}/${userId}`,
      type: 'DELETE',
      success: function(result) {
        // Handle success e.g.remove the deleted review from the UI
        console.log('Review deleted:', result);
        $(`li[data-id=${reviewId}]`).remove();
      },
      error: function(xhr, status, error) {
        // Handle error
        console.error('Error deleting review:', status, error);
      }
    });
  };
$(document).ready(function () {
    $('ul.books').on('click', '.delete', function () {
        const userId = $('ul.books').data('user-id');
        const reviewId = $(this).data('id');
        deleteReview(reviewId, userId);
    });
});