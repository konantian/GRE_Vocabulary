DROP TABLE IF EXISTS yaoniming3000;
DROP TABLE IF EXISTS other;

CREATE TABLE yaoniming3000 (
	id 				   INT,
	word	   		   TEXT,
	meaning	           TEXT,
	date_when_inserted DATE,
	PRIMARY KEY (id)
);

CREATE TABLE other (
	id 				   INT,
	word	   		   TEXT,
	meaning	           TEXT,
	date_when_inserted DATE,
	PRIMARY KEY (id)
);

INSERT INTO yaoniming3000 VALUES(1,'affect','v.假装,倾向,喜欢,影响',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'modest','adj.适中的,适量的,谦虚的',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'temper','v.缓和,调整 n.脾气',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'algae','n.藻类',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'ballon','v.激增 n.气球',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'compelling','adj.有吸引力的,令人信服的,强大的',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'dispute','v.争论,质疑 n.争论,纠纷',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'striking','adj.引人注目的,显著地',date('now','localtime'));

INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'thrust','v.猛推,刺,插 n.插入,挤,主旨',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'accessible','adj.容易理解的,容易到达的,易获得的',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'adequate','adj.足够的,充分的,适当的,合格的',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'affinity','n.喜爱,亲和力,类同',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'appreciate','v.意识到,欣赏,感激,升值',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'ascetic','adj.清苦的,苦行的',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'assume','v.假设,承担,呈现',date('now','localtime'));
INSERT INTO yaoniming3000 VALUES((select max(id)+1 from yaoniming3000),'block','v.阻止',date('now','localtime'));