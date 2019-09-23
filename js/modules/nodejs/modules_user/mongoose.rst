mongoose
========

.. code-block:: js

    const mongoose = require('mongoose');

    mongoose.connect('mongodb://localhost:27017/collection_name', {});

    mongoose.Promise = require('bluebird');


.. code-block:: js

    // messages.model.js

    const mongoose = require('mongoose');
    const Schema = mongoose.Schema;

    const MessageSchema = new Schema({
        date: {
            type: Date,
            default: Date.now
        },
        content: {
            type: String
        },
        username: {
            type: String
        }
    }, {
        versionKey: false,
        collection: 'MessageCollection'
    });

    MessageSchema.pre('save', function(next){
        if (this.isModified('date') || this.isNew()){
            this.date = new Date();
        }
        next();
    });

    module.exports = mongoose.model('MessageModel', MessageSchema);