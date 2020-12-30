 $(document).ready(function(){

   var private_socket = io('http://127.0.0.1:5000/private')

   $('#send_username').on('click',function() {
     private_socket.emit('username',$('#username').val());
   });
});
