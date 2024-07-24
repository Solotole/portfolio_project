function updateReview(reviewId, userId, updatedData) {
  // fuction responsible for updating a review
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
  // checking if user clicked on update
  $('ul.books').on('click', '.update', function () {
    // Accessing review id of the review
    const reviewId = $(this).closest('li').data('id');
    // Accessing user id
    const userId = $('ul.books').data('user-id');
    // prompting for user new comment input
    const newComment= prompt('Enter new review comment:');
    // prompting for user new rate input 
    const newRating = prompt('Enter new rating:');
    // checking if user entered input
    if (newRating && newComment) {
      const updatedReview = {
        rating: newRating,
        text: newComment
      };
      updateReview(reviewId, userId, updatedReview);
    } else {
      alert('Inpu required!');
    }
  });
});