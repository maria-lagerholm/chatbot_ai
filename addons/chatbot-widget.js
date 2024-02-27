document.addEventListener('DOMContentLoaded', (event) => {
    // Create chatbot icon container
    var chatbotIconContainer = document.createElement('div');
    chatbotIconContainer.id = 'chatbot-icon';
    chatbotIconContainer.style.position = 'fixed';
    chatbotIconContainer.style.bottom = '10px';
    chatbotIconContainer.style.right = '10px';
    chatbotIconContainer.style.cursor = 'pointer';
    chatbotIconContainer.style.zIndex = '10000';
    chatbotIconContainer.innerHTML = '<img src="path/to/your/icon.png" alt="Chatbot Icon" />';
    
    // Create chatbot iframe container
    var chatbotIframeContainer = document.createElement('div');
    chatbotIframeContainer.classList.add('html-embed-7', 'w-embed', 'w-iframe');
    chatbotIframeContainer.style.display = 'none';
    chatbotIframeContainer.style.position = 'fixed';
    chatbotIframeContainer.style.bottom = '50px';
    chatbotIframeContainer.style.right = '10px';
    chatbotIframeContainer.style.zIndex = '10000';
    chatbotIframeContainer.style.backgroundColor = 'white';
    chatbotIframeContainer.style.border = '1px solid #ccc';
    chatbotIframeContainer.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
    chatbotIframeContainer.innerHTML = '<iframe id="chatbot-iframe" src="" height="450" style="width:100%;border:none;"></iframe>';

    // Append both containers to the body
    document.body.appendChild(chatbotIconContainer);
    document.body.appendChild(chatbotIframeContainer);

    // Add event listener to chatbot icon to toggle iframe visibility and set src attribute
    chatbotIconContainer.addEventListener('click', function() {
        if (chatbotIframeContainer.style.display === 'none') {
            chatbotIframeContainer.style.display = 'block';
            document.getElementById('chatbot-iframe').src = "https://chatbot-web.streamlit.app/?embed=true&embed_options=light_theme&embed_options=disable_scrolling";
        } else {
            chatbotIframeContainer.style.display = 'none';
            document.getElementById('chatbot-iframe').src = "";
        }
    });
});
