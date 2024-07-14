function updateReview(reviewId, userId, updatedData) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/reviews/${reviewId}/${userId}`,
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify(updatedData),
      success: function(result) {
        // Handle success (e.g., update the review in the UI)
        console.log('Review updated:', result);
        const $reviewItem = $(`li[data-id=${reviewId}]`);
        $reviewItem.find('.reviewcomment').text(`review: ${updatedData.text}`);
        $reviewItem.find('.reviewrating').text(`rate: ${updatedData.rating}`);
      },
      error: function(xhr, status, error) {
        // Handle error
        console.error('Error updating review:', status, error);
      }
    });
};
$(document).ready(function () {
    $('ul.books').on('click', '.update', function () {
        const reviewId = $(this).closest('li').data('id');
        const userId = $('ul.books').data('user-id');
        const newComment= prompt('Enter new review comment:');
        const newRating = prompt('Enter new rating:');
        if (newRating && newComment) {
          const updatedReview = {
            rating: newRating,
            text: newComment
          };
          updateReview(reviewId, userId, updatedReview);
        }
    });
});