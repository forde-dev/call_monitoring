DROP TABLE IF EXISTS call_incoming;
CREATE TABLE call_incoming
(
    system_id CHAR(9),
    user VARCHAR(30),
    call_date DATE,
    time CHAR(8),
    line CHAR(1),
    incoming_num VARCHAR(15),
    ext CHAR(3),
    ddi CHAR(4)
);

DROP TABLE IF EXISTS call_logs;
CREATE TABLE call_logs
(
    system_id CHAR(9),
    user VARCHAR(30),
    call_date DATE,
    time CHAR(8),
    line CHAR(1),
    answered VARCHAR(3),
    number VARCHAR(15),
    ring CHAR(5),
    duration CHAR(8),
    ext CHAR(3),
    ddi CHAR(4)
);

DROP TABLE IF EXISTS call_outgoing;
CREATE TABLE call_outgoing
(
    system_id CHAR(9),
    user VARCHAR(30),
    call_date DATE,
    time CHAR(8),
    line CHAR(1),
    answered VARCHAR(3),
    number VARCHAR(15),
    ext CHAR(3)
);
