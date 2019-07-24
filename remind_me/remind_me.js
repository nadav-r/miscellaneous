const yargs = require('yargs');
const notifier = require('node-notifier');
const path = require('path');



const beep = () => console.log('\007')

const setReminder = (task, time) => {
    milliseconds = time * 60 * 1000
    console.log('You\'ll be notified every ' + time + ' minutes')
    setInterval(() => {
        //string
        notifier.notify(task);

        // Object
        notifier.notify({
            title: 'My notification',
            message: 'Hello, there!',
        });
    }, milliseconds);
}

yargs.command({
    command: '$0',
    describe: 'Set up scheduled notification for a task',
    builder: {
        task: {
            describe: 'Task name',
            demandOption: true,
            type: 'string'
        },
        time: {
            describe: 'Set up interval for notification in minutes',
            demandOption: true,
            type: 'int'
        }
    },
    handler(argv) {
        setReminder(argv.task, argv.time)
    }

})
    .argv


