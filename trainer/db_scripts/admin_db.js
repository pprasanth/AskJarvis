// install mongosh to run this script.
// once you install the mongosh and then run mongosh in terminal
// and run "load("<path to project>/AIChatbot/trainer/scripts/admin_db.js");"
// Admin role is 1001
// Connect to DB
db = connect( 'mongodb://localhost/chatterbot-database' );
// Create and add entries to users collections
db.users.insertMany( [
    {
       username: 'admin',
       password: '0192023a7bbd73250516f069df18b500', // admin123
       role: [1001]
    }
]);
