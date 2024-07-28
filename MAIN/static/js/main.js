// Function to hide the icon bar and show the navigation menu
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");  // Get the element with ID 'iconBar'
    var navigation = document.getElementById("navigation");  // Get the element with ID 'navigation'
    iconBar.setAttribute("style", "display:none;");  // Set the display style of 'iconBar' to none (hide it)
    navigation.classList.remove("hide");  // Remove the 'hide' class from the 'navigation' element (show it)
}

// Function to show the icon bar and hide the navigation menu
function showIconBar(){
    var iconBar = document.getElementById("iconBar");  // Get the element with ID 'iconBar'
    var navigation = document.getElementById("navigation");  // Get the element with ID 'navigation'
    iconBar.setAttribute("style", "display:block;");  // Set the display style of 'iconBar' to block (show it)
    navigation.classList.add("hide");  // Add the 'hide' class to the 'navigation' element (hide it)
}

// Function to show the comment area
function showComment(){
    var commentArea = document.getElementById("comment-area");  // Get the element with ID 'comment-area'
    commentArea.classList.remove("hide");  // Remove the 'hide' class from the 'comment-area' element (show it)
}

// Function to show the reply area
function showReply(commentId){
    var replyArea = document.getElementById(commentId);  // Get the element with ID 'reply-area'
    replyArea.classList.remove("hide");  // Remove the 'hide' class from the 'reply-area' element (show it)
}