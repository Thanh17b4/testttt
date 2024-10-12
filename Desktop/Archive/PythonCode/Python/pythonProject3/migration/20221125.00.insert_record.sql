INSERT INTO jobs (name, level, cv_language, type, slug, company_id,  due_at, salary)
VALUES ("Chuyen vien tin dung", "Nhân viên", "Bất kỳ", "toan thoi gian", "chuyen-gia-ngan-sach-tai-chinh-va-ke-hoach", 3, "2022-12-13", "Thoả thuận");

INSERT INTO job_location(job_id, location_id) VALUES (37, 1);
INSERT INTO job_category(job_id, category_id)
VALUES
(37, 1),
(37, 2);

INSERT INTO job_benefits(job_id, benefit_id) VALUES (37, 1);

INSERT INTO locations(name, slug)
VALUES
("Ha Noi", "ha-noi"),
("Ha Nam", "ha-nam");

INSERT INTO categories(name, slug)
VALUES
("Chứng khoán", "chung-khoan"),
("Tài chính kế toán ", "tai-chinh-ke-toan");

INSERT INTO benefits(name, slug)
VALUES
("Trợ cấp đi lại", "tro-cap-di-lai"),
("du lịch", "du-lich");

INSERT INTO company(name, address, website, scale, contact, slug)
VALUES
("Techcombank", "Hội sở Miền Bắc: Số 191 Bà Triệu, Phường Lê Đại Hành, Quận Hai Bà Trưng, Hà NộiHội sở Miền Nam: Tòa nhà Lim Tower, số 9-11 Tôn Đức Thắng, Quận 1, TP Hồ Chí Minh", "https://techcombankjobs.com/", "10.000-20.000 nhân viên", "techcombank", "Phong nhan su"),
("Ngân Hàng Thương Mại Cổ Phần Quân Đội - MB", "HN: tòa nhà MB số 18 Lê Văn Lương, Cầu giấy , HCM: Sunny tower, 259 Trần Hưng Đạo, Q1, TPHCM", "https://www.mbbank.com.vn/|Mạng xã hộiTheo dõi (787)", "500-999 nhân viên", "ngan-hang-thuong-mai-co-phan-quan-doi-mb", "Phong nhan su");