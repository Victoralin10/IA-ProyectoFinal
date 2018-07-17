const router = require('express').Router();
const fs = require('fs');
const path = require('path');


router.get('/', (req, res, next) => {
    res.render('tool');
});

router.get('/files', (req, res, next) => {
    fs.readdir(path.join(__dirname, '..', 'public', 'data'), (err , files) => {
        if (err) {
            return res.send({success: false});
        }

        files = files.sort().map(file => {
            let tm = file.split('.')[0];
            let i = 0;
            while (tm[i] < '0' || tm[i] > '9') i++;
            tm = tm.substr(i);
            tm = parseInt(tm)*1000;

            return {
                file_name: file,
                timestamp: tm
            };
        });

        res.json({success: true, data: files});
    });
});

module.exports = router;