const router = require('express').Router();

const dbConn = require('../database/mysql');


/* GET users listing. */
router.get('/events', function(req, res, next) {

  let sql = 'select * from events order by id desc limit 100';
  dbConn.queryAsync(sql)
      .then(rows => {
        res.json({
            success: true,
            data: rows
        });
      })
      .catch(next);
});

module.exports = router;
