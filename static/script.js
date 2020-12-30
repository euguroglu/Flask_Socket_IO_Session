 $(document).ready(function(){

   var private_socket = io('http://127.0.0.1:5000/private')

   $('#send_username').on('click',function() {
     private_socket.emit('username',$('#username').val());
   });

   $('#send_private_message').on('click',function(){
     var recipient = $('#send_to_username').val();
     var message_to_send = $('#private_message').val();
     private_socket.emit('private_message',{'username':recipient,'message':message_to_send});
   });

   private_socket.on('new_private_message',function(msg){
     alert(msg);
   });

   $('#join_room').on('click',function() {
     var room = $('#room_to_join').val();

     private_socket.emit('join_room',room);
   });

   private_socket.on('room_message',function(msg){
     alert(msg);
   });

});
