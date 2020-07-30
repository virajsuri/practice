#!/usr/bin/env python

import glob
import pandas as pd
import os, sys
import tr_grab
import sd_grab
import lbus_grab
import lgc3_grab
import psycopg2
from psycopg2 import sql
import overwrite_eof as o
import pyPull, views, cmoPull, corPull, outlookParser, security2db, cashCheck
import time
import datetime
# from win32com.client import Dispatch

def add_columns():
	print("   Working...")
	o.run(o.tr_f_xlsx, o.tr_f_csv, o.sd_f_xlsx, o.sd_f_csv, o.lb_f_xlsx, o.lb_f_csv, o.lg_f_xlsx, o.lg_f_csv)

	# ===================================================

	df = pd.read_csv(o.tr_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['ctd'] = 1
	df.to_csv(o.tr_f_csv, sep='|')
	cashCheck.check(df, 'Total Return')

	df = pd.read_csv(o.sd_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['ctd'] = 1
	df.to_csv(o.sd_f_csv, sep='|')
	cashCheck.check(df, 'Short Duration')

	df = pd.read_csv(o.lb_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['ctd'] = 1
	df.to_csv(o.lb_f_csv, sep='|')

	df = pd.read_csv(o.lg_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['ctd'] = 1
	df.to_csv(o.lg_f_csv, sep='|')

	# ===================================================

	df = pd.read_csv(o.tr_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['date'] = 'd'
	df.to_csv(o.tr_f_csv, sep='|')

	df = pd.read_csv(o.sd_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['date'] = 'd'
	df.to_csv(o.sd_f_csv, sep='|')

	df = pd.read_csv(o.lb_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['date'] = 'd'
	df.to_csv(o.lb_f_csv, sep='|')

	df = pd.read_csv(o.lg_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['date'] = 'd'
	df.to_csv(o.lg_f_csv, sep='|')

	# ===================================================

	df = pd.read_csv(o.tr_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['id_portfolio'] = ''
	df.to_csv(o.tr_f_csv, sep='|')

	df = pd.read_csv(o.sd_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['id_portfolio'] = ''
	df.to_csv(o.sd_f_csv, sep='|')

	df = pd.read_csv(o.lb_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['id_portfolio'] = ''
	df.to_csv(o.lb_f_csv, sep='|')

	df = pd.read_csv(o.lg_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['id_portfolio'] = ''
	df.to_csv(o.lg_f_csv, sep='|')

	# ===================================================

	df = pd.read_csv(o.tr_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder'] = ''
	df.to_csv(o.tr_f_csv, sep='|')

	df = pd.read_csv(o.sd_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder'] = ''
	df.to_csv(o.sd_f_csv, sep='|')

	df = pd.read_csv(o.lb_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder'] = ''
	df.to_csv(o.lb_f_csv, sep='|')

	df = pd.read_csv(o.lg_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder'] = ''
	df.to_csv(o.lg_f_csv, sep='|')

	# ===================================================

	df = pd.read_csv(o.tr_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder2'] = ''
	df.to_csv(o.tr_f_csv, sep='|')

	df = pd.read_csv(o.sd_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder2'] = ''
	df.to_csv(o.sd_f_csv, sep='|')

	df = pd.read_csv(o.lb_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder2'] = ''
	df.to_csv(o.lb_f_csv, sep='|')

	df = pd.read_csv(o.lg_f_csv, delimiter='|', error_bad_lines=False, index_col=0)
	df['placeholder2'] = ''
	df.to_csv(o.lg_f_csv, sep='|')

	# ===================================================

	print("Files moved to proper directories.")

def connect():
	conn = None
	try:
		conn = psycopg2.connect(host="192.168.65.1", port="5432", database="mp", user="SmithCap", password="SmithCap01!")
		cur = conn.cursor()
		print("\n")
		print("Established new connection to host aws on port 5432, database 'mp' as user 'postgres'")
		print('PostgreSQL database version:')

		cur.execute('SELECT version()')

		db_version = cur.fetchone()
		print(db_version)

		cur.close()

	except (Exception, psycopg2.DatabaseError) as e:
		print(e)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed')

def create_table():
	conn = None
	try:
		conn = psycopg2.connect(host="smithcap.csxebhnt39o6.us-west-2.rds.amazonaws.com", port="5432", database="mp", user="SmithCap", password="SmithCap01!")
		cur = conn.cursor()
		print("\n")
		print("Established new connection to host aws on port 5432, database 'mp' as user 'postgres'")

		# =========== CAREFUL EXECUTING THE FOLLOWING 2 LINES ===========
		cur.execute("DROP TABLE IF EXISTS securities CASCADE;")
		print("Table \"securities\" dropped")
		cur.execute("CREATE TABLE securities (id_security INTEGER, nm VARCHAR(128), cusip VARCHAR(16), weight DOUBLE PRECISION, oad DOUBLE PRECISION, ytw DOUBLE PRECISION, ytm DOUBLE PRECISION, oas DOUBLE PRECISION, oasd DOUBLE PRECISION, oac DOUBLE PRECISION, mty DOUBLE PRECISION, px_close DOUBLE PRECISION, amt_out DOUBLE PRECISION, sp VARCHAR(6), fitch VARCHAR(6), rating VARCHAR(6), cpn DOUBLE PRECISION, krd_6m DOUBLE PRECISION, krd_2y DOUBLE PRECISION, krd_5y DOUBLE PRECISION, krd_10y DOUBLE PRECISION, krd_20y DOUBLE PRECISION, krd_30y DOUBLE PRECISION, bclass1 VARCHAR(64), bclass2 VARCHAR(64), bclass3 VARCHAR(64), bclass4 VARCHAR(64), ticker VARCHAR(32), ctd DOUBLE PRECISION, date varchar(32), id_portfolio INTEGER, placeholder VARCHAR(2), placeholder2 VARCHAR(2))")
		print("Table \"securities\" recreated")
		# cur.execute("")
		# ===============================================================
		cur.close()

		conn.commit()

		views.drop_views()
		views.create_views()
	except (Exception, psycopg2.DatabaseError) as e:
		print(e)
	finally:
		if conn is not None:
			conn.close()


def import_data(tr, sd, lb, lg):
	print("\n")
	print("Data Import")
	print("===========")
	conn = None
	try:
		conn = psycopg2.connect(host="smithcap.csxebhnt39o6.us-west-2.rds.amazonaws.com", port="5432", database="mp", user="SmithCap", password="SmithCap01!")
		cur = conn.cursor()
		print("Established new connection to host aws on port 5432, database 'mp' as user 'postgres'")

	# ====================== DROP IF OVERWRITING SAME DAY ENTRY ======================
		cur.execute("DELETE FROM securities WHERE date = to_char(CURRENT_DATE, 'YYYY-MM-DD')")

	# ====================== COPY FROM CSV ======================
		# =================== Total Return ===================
		sqltr = "COPY securities FROM STDIN DELIMITER '|' CSV"
		with open(tr, 'r', encoding='utf-8') as f:
		    next(f)  # Skip the header row.
		    cur.copy_expert(sqltr, f)

		cur.execute("UPDATE securities SET id_portfolio = 1")
		print("  securities added to 'securities' table from Total Return file")

		# ================== Short Duration ==================
		sqlsd = "COPY securities FROM STDIN DELIMITER '|' CSV"
		with open(sd, 'r', encoding='utf-8') as sd_f:
		    next(sd_f)  # Skip the header row.
		    cur.copy_expert(sqlsd, sd_f)

		cur.execute("UPDATE securities SET id_portfolio = 2 WHERE id_portfolio IS null")
		print("  securities added to 'securities' table from Short Duration file")

		# ===================== LBUSSTAT =====================
		sqllb = "COPY securities FROM STDIN DELIMITER '|' CSV"
		with open(lb, 'r', encoding='utf-8') as f:
		    next(f)  # Skip the header row.
		    cur.copy_expert(sqllb, f)

		cur.execute("UPDATE securities SET id_portfolio = 3 WHERE id_portfolio IS null")
		print("  securities added to 'securities' table from LBUSSTAT file")

		# ===================== LGC3STAT =====================
		sqllg = "COPY securities FROM STDIN DELIMITER '|' CSV"
		with open(lg, 'r', encoding='utf-8') as f:
		    next(f)  # Skip the header row.
		    cur.copy_expert(sqllg, f)

		yy=o.tr_f_csv[-6:-4]
		mm=o.tr_f_csv[-10:-8]
		dd=o.tr_f_csv[-8:-6]
		dt="20"+yy+"-"+mm+"-"+dd
		cur.execute("UPDATE securities SET id_portfolio = 4 WHERE id_portfolio IS null")
		print("  securities added to 'securities' table from LGC3STAT file")
		print("		Finishing...")

		cur.execute(sql.SQL("UPDATE securities SET \"date\" = %s WHERE \"date\" = 'd'"), [dt])
		cur.execute(sql.SQL("UPDATE securities SET ctd=(weight*oad)/100 WHERE \"date\" = %s"), [dt])

		cur.close()

		print("			Connection closed.")
		print("		Committing changes...")

		conn.commit()
		print("			Changes committed.")

	except (Exception, psycopg2.DatabaseError) as e:
		print(e)
	finally:
		if conn is not None:
			conn.close()

def export_data():
	print("\n")
	print("Data Export")
	print("===========")
	conn = None
	try:
		conn = psycopg2.connect(host="smithcap.csxebhnt39o6.us-west-2.rds.amazonaws.com", port="5432", database="mp", user="SmithCap", password="SmithCap01!")
		cur = conn.cursor()
		print("Established new connection to host aws on port 5432, database 'mp' as user 'postgres'")
	#
	# ==============================================================================
	# ============================= mp Database Build ==============================
	# ==============================================================================
	#

	# Definitions

		cwd=o.cwd
		dayspec=o.dayspec
		ext_csv='.csv'
		ext_xlsx='.xlsx'

		file_tr_rel=cwd+o.tr_rel+o.dayspec+ext_csv
		file_sd_rel=cwd+o.sd_rel+o.dayspec+ext_csv
		file_lb_rel=cwd+o.lb_rel+o.dayspec+ext_csv
		file_lg_rel=cwd+o.lg_rel+o.dayspec+ext_csv

		tr_s_rel="02. PORT DATA\\Total Return\\CUSIP\\tr_cusip"
		tr_s_corp_rel="02. PORT DATA\\Total Return\\CUSIP\\tr_cusip_corp"
		tr_s_corp_grouped_rel="02. PORT DATA\\Total Return\\CUSIP\\tr_cusip_corp_grouped"
		tr_t_in_rel="02. PORT DATA\\Total Return\\Ticker\\tr_ticker_in"
		tr_t_out_rel="02. PORT DATA\\Total Return\\Ticker\\tr_ticker_out"
		tr_c_rel="02. PORT DATA\\Total Return\\Class\\tr_class"
		tr_r_rel="02. PORT DATA\\Total Return\\Ratings\\tr_ratings"
		tr_r_corp_rel="02. PORT DATA\\Total Return\\Ratings\\tr_ratings_corp"
		tr_l_rel="02. PORT DATA\\Total Return\\Maturity\\tr_mty"
		tr_l_corp_rel="02. PORT DATA\\Total Return\\Maturity\\tr_mty_corp"

		sd_s_rel="02. PORT DATA\\Short Duration\\CUSIP\\sd_cusip"
		sd_s_corp_rel="02. PORT DATA\\Short Duration\\CUSIP\\sd_cusip_corp"
		sd_s_corp_grouped_rel="02. PORT DATA\\Short Duration\\CUSIP\\sd_cusip_corp_grouped"
		sd_t_in_rel="02. PORT DATA\\Short Duration\\Ticker\\sd_ticker_in"
		sd_t_out_rel="02. PORT DATA\\Short Duration\\Ticker\\sd_ticker_out"
		sd_c_rel="02. PORT DATA\\Short Duration\\Class\\sd_class"
		sd_r_rel="02. PORT DATA\\Short Duration\\Ratings\\sd_ratings"
		sd_r_corp_rel="02. PORT DATA\\Short Duration\\Ratings\\sd_ratings_corp"
		sd_l_rel="02. PORT DATA\\Short Duration\\Maturity\\sd_mty"
		sd_l_corp_rel="02. PORT DATA\\Short Duration\\Maturity\\sd_mty_corp"

		lb_s_rel="02. PORT DATA\\BB Agg\\CUSIP\\lb_cusip"
		lb_s_corp_rel="02. PORT DATA\\BB Agg\\CUSIP\\lb_cusip_corp"
		lb_t_rel="02. PORT DATA\\BB Agg\\Ticker\\lb_ticker"
		lb_t_top3_rel="02. PORT DATA\\BB Agg\\Ticker\\lb_ticker_top"
		lb_c_rel="02. PORT DATA\\BB Agg\\Class\\lb_class"
		lb_l_rel="02. PORT DATA\\BB Agg\\Maturity\\lb_mty"
		lb_l_corp_rel="02. PORT DATA\\BB Agg\\Maturity\\lb_mty_corp"

		lg_s_rel="02. PORT DATA\\BB Gov Cred 1-3\\CUSIP\\lg_cusip"
		lg_s_corp_rel="02. PORT DATA\\BB Gov Cred 1-3\\CUSIP\\lg_cusip_corp"
		lg_t_rel="02. PORT DATA\\BB Gov Cred 1-3\\Ticker\\lg_ticker"
		lg_c_rel="02. PORT DATA\\BB Gov Cred 1-3\\Class\\lg_class"
		lg_l_rel="02. PORT DATA\\BB Gov Cred 1-3\\Maturity\\lg_mty"
		lg_l_corp_rel="02. PORT DATA\\BB Gov Cred 1-3\\Maturity\\lg_mty_corp"

		totals_rel="02. PORT DATA\\Totals\\totals"

		# =====================================================================

		file_tr_cusip = os.path.join(cwd, tr_s_rel + dayspec + ext_csv)
		file_tr_cusip_corp = os.path.join(cwd, tr_s_corp_rel + dayspec + ext_csv)
		file_tr_cusip_corp_grouped = os.path.join(cwd, tr_s_corp_grouped_rel + dayspec + ext_csv)
		file_tr_ticker_in = os.path.join(cwd, tr_t_in_rel + dayspec + ext_csv)
		file_tr_ticker_out = os.path.join(cwd, tr_t_out_rel + dayspec + ext_csv)
		file_tr_class = os.path.join(cwd, tr_c_rel + dayspec + ext_csv)
		file_tr_ratings = os.path.join(cwd, tr_r_rel + dayspec + ext_csv)
		file_tr_ratings_corp = os.path.join(cwd, tr_r_corp_rel + dayspec + ext_csv)
		file_tr_l = os.path.join(cwd, tr_l_rel + dayspec + ext_csv)
		file_tr_l_corp = os.path.join(cwd, tr_l_corp_rel + dayspec + ext_csv)

		file_sd_cusip = os.path.join(cwd, sd_s_rel + dayspec + ext_csv)
		file_sd_cusip_corp = os.path.join(cwd, sd_s_corp_rel + dayspec + ext_csv)
		file_sd_cusip_corp_grouped = os.path.join(cwd, sd_s_corp_grouped_rel + dayspec + ext_csv)
		file_sd_ticker_in = os.path.join(cwd, sd_t_in_rel + dayspec + ext_csv)
		file_sd_ticker_out = os.path.join(cwd, sd_t_out_rel + dayspec + ext_csv)
		file_sd_class = os.path.join(cwd, sd_c_rel + dayspec + ext_csv)
		file_sd_ratings = os.path.join(cwd, sd_r_rel + dayspec + ext_csv)
		file_sd_ratings_corp = os.path.join(cwd, sd_r_corp_rel + dayspec + ext_csv)
		file_sd_l = os.path.join(cwd, sd_l_rel + dayspec + ext_csv)
		file_sd_l_corp = os.path.join(cwd, sd_l_corp_rel + dayspec + ext_csv)

		file_lb_cusip = os.path.join(cwd, lb_s_rel + dayspec + ext_csv)
		file_lb_cusip_corp = os.path.join(cwd, lb_s_corp_rel + dayspec + ext_csv)
		file_lb_ticker = os.path.join(cwd, lb_t_rel + dayspec + ext_csv)
		file_lb_top3_ticker = os.path.join(cwd, lb_t_top3_rel + dayspec + ext_csv)
		file_lb_class = os.path.join(cwd, lb_c_rel + dayspec + ext_csv)
		file_lb_l = os.path.join(cwd, lb_l_rel + dayspec + ext_csv)
		file_lb_l_corp = os.path.join(cwd, lb_l_corp_rel + dayspec + ext_csv)

		file_lg_cusip = os.path.join(cwd, lg_s_rel + dayspec + ext_csv)
		file_lg_cusip_corp = os.path.join(cwd, lg_s_corp_rel + dayspec + ext_csv)
		file_lg_ticker = os.path.join(cwd, lg_t_rel + dayspec + ext_csv)
		file_lg_class = os.path.join(cwd, lg_c_rel + dayspec + ext_csv)
		file_lg_l = os.path.join(cwd, lg_l_rel + dayspec + ext_csv)
		file_lg_l_corp = os.path.join(cwd, lg_l_corp_rel + dayspec + ext_csv)

		file_totals = os.path.join(cwd, totals_rel + dayspec + ext_csv)

		# =====================================================================

		trc = "COPY (SELECT * FROM tr_s) TO STDOUT WITH CSV HEADER"
		trcc = "COPY (SELECT * FROM tr_s_corp) TO STDOUT WITH CSV HEADER"
		trcg = "COPY (SELECT * FROM tr_s_corp_grouped) TO STDOUT WITH CSV HEADER"
		trti = "COPY (SELECT * FROM tr_t_in) TO STDOUT WITH CSV HEADER"
		trto = "COPY (SELECT * FROM tr_t_out) TO STDOUT WITH CSV HEADER"
		trcl = "COPY (SELECT * FROM tr_c) TO STDOUT WITH CSV HEADER"
		trr = "COPY (SELECT * FROM tr_r) TO STDOUT WITH CSV HEADER"
		trrc = "COPY (SELECT * FROM tr_r_corp) TO STDOUT WITH CSV HEADER"
		trl = "COPY (SELECT * FROM tr_l) TO STDOUT WITH CSV HEADER"
		trlc = "COPY (SELECT * FROM tr_l_corp) TO STDOUT WITH CSV HEADER"

		sdc = "COPY (SELECT * FROM sd_s) TO STDOUT WITH CSV HEADER"
		sdcc = "COPY (SELECT * FROM sd_s_corp) TO STDOUT WITH CSV HEADER"
		sdcg = "COPY (SELECT * FROM sd_s_corp_grouped) TO STDOUT WITH CSV HEADER"
		sdti = "COPY (SELECT * FROM sd_t_in) TO STDOUT WITH CSV HEADER"
		sdto = "COPY (SELECT * FROM sd_t_out) TO STDOUT WITH CSV HEADER"
		sdcl = "COPY (SELECT * FROM sd_c) TO STDOUT WITH CSV HEADER"
		sdr = "COPY (SELECT * FROM sd_r) TO STDOUT WITH CSV HEADER"
		sdrc = "COPY (SELECT * FROM sd_r_corp) TO STDOUT WITH CSV HEADER"
		sdl = "COPY (SELECT * FROM sd_l) TO STDOUT WITH CSV HEADER"
		sdlc = "COPY (SELECT * FROM sd_l_corp) TO STDOUT WITH CSV HEADER"

		lbc = "COPY (SELECT * FROM lb_s) TO STDOUT WITH CSV HEADER"
		lbcc = "COPY (SELECT * FROM lb_s_corp) TO STDOUT WITH CSV HEADER"
		lbt = "COPY (SELECT * FROM lb_t) TO STDOUT WITH CSV HEADER"
		lbtt = "COPY (SELECT * FROM lb_t_top3) TO STDOUT WITH CSV HEADER"
		lbcl = "COPY (SELECT * FROM lb_c) TO STDOUT WITH CSV HEADER"
		lbl = "COPY (SELECT * FROM lb_l) TO STDOUT WITH CSV HEADER"
		lblc = "COPY (SELECT * FROM lb_l_corp) TO STDOUT WITH CSV HEADER"

		lgc = "COPY (SELECT * FROM lg_s) TO STDOUT WITH CSV HEADER"
		lgcc = "COPY (SELECT * FROM lg_s_corp) TO STDOUT WITH CSV HEADER"
		lgt = "COPY (SELECT * FROM lg_t) TO STDOUT WITH CSV HEADER"
		lgcl = "COPY (SELECT * FROM lg_c) TO STDOUT WITH CSV HEADER"
		lgl = "COPY (SELECT * FROM lg_l) TO STDOUT WITH CSV HEADER"
		lglc = "COPY (SELECT * FROM lg_l_corp) TO STDOUT WITH CSV HEADER"

		totl = "COPY (SELECT * FROM totals) TO STDOUT WITH CSV HEADER"

	# Queries

	# ================= Total Return ================
		with open(file_tr_cusip, 'w', encoding='utf-8') as f:
			cur.copy_expert(trc, f)
			print("Copied: trc")
		with open(file_tr_cusip_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(trcc, f)
			print("Copied: trcc")
		with open(file_tr_cusip_corp_grouped, 'w', encoding='utf-8') as f:
			cur.copy_expert(trcg, f)
			print("Copied: trcg")
		with open(file_tr_ticker_in, 'w', encoding='utf-8') as f:
			cur.copy_expert(trti, f)
			print("Copied: trci")
		with open(file_tr_ticker_out, 'w', encoding='utf-8') as f:
			cur.copy_expert(trto, f)
			print("Copied: trco")
		with open(file_tr_class, 'w', encoding='utf-8') as f:
			cur.copy_expert(trcl, f)
			print("Copied: trcl")
		with open(file_tr_ratings, 'w', encoding='utf-8') as f:
			cur.copy_expert(trr, f)
			print("Copied: trr")
		with open(file_tr_ratings_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(trrc, f)
			print("Copied: trrc")
		with open(file_tr_l, 'w', encoding='utf-8') as f:
			cur.copy_expert(trl, f)
			print("Copied: trl")
		with open(file_tr_l_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(trlc, f)
			print("Copied: trlc")
		print("Total Return files created")
	# ================ Short Duration =================
		with open(file_sd_cusip, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdc, f)
			print("Copied: sdc")
		with open(file_sd_cusip_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdcc, f)
			print("Copied: sdcc")
		with open(file_sd_cusip_corp_grouped, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdcg, f)
			print("Copied: sdcg")
		with open(file_sd_ticker_in, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdti, f)
			print("Copied: sdci")
		with open(file_sd_ticker_out, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdto, f)
			print("Copied: sdco")
		with open(file_sd_class, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdcl, f)
			print("Copied: sdcl")
		with open(file_sd_ratings, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdr, f)
			print("Copied: sdr")
		with open(file_sd_ratings_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdrc, f)
			print("Copied: sdrc")
		with open(file_sd_l, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdl, f)
			print("Copied: sdl")
		with open(file_sd_l_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(sdlc, f)
			print("Copied: sdlc")
		print("Short Duration files created")
	# ================== LBUSSTAT =====================
		with open(file_lb_cusip, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbc, f)
			print("Copied: ldc")
		with open(file_lb_cusip_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbcc, f)
			print("Copied: ldcc")
		with open(file_lb_ticker, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbt, f)
			print("Copied: lbt")
		with open(file_lb_top3_ticker, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbtt, f)
			print("Copied: ldtt")
		with open(file_lb_class, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbcl, f)
			print("Copied: ldcl")
		with open(file_lb_l, 'w', encoding='utf-8') as f:
			cur.copy_expert(lbl, f)
			print("Copied: ldl")
		with open(file_lb_l_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(lblc, f)
			print("Copied: ldlc")
		print("LBUSSTAT files created")
	# ================== LGC3STAT =====================
		with open(file_lg_cusip, 'w', encoding='utf-8') as f:
			cur.copy_expert(lgc, f)
			print("Copied: lgc")
		with open(file_lg_cusip_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(lgcc, f)
			print("Copied: lgcc")
		with open(file_lg_ticker, 'w', encoding='utf-8') as f:
			cur.copy_expert(lgt, f)
			print("Copied: lgt")
		with open(file_lg_class, 'w', encoding='utf-8') as f:
			cur.copy_expert(lgcl, f)
			print("Copied: lgcl")
		with open(file_lg_l, 'w', encoding='utf-8') as f:
			cur.copy_expert(lgl, f)
			print("Copied: lgl")
		with open(file_lg_l_corp, 'w', encoding='utf-8') as f:
			cur.copy_expert(lglc, f)
			print("Copied: lglc")
		print("LGC3STAT files created")
	# =================================================
		with open(file_totals, 'w', encoding='utf-8') as f:
			cur.copy_expert(totl, f)

		cur.close()
		conn.commit()

		# ================================ Start mp_v4 =================================

		# xl = Dispatch("Excel.Application")
		# xl.Visible = True # otherwise excel is hidden

		# wb = xl.Workbooks.Open(r'C:\Users\mccur\Datto Workplace\Research\Morning Packet\Morning PACKET\mp.xlsm')
		# # wb.Close()
		# # xl.Quit()
		# print("Opening Morning Packet Excel sheet...")

	except (Exception, psycopg2.DatabaseError) as e:
		print(e)
	finally:
		if conn is not None:
			conn.close()

if __name__ == '__main__':
	start = time.time()
	# print("Getting MorningStar Report from Outlook...")
	# outlookParser.morningStarReportDownload()
	# print("MorningStar Report saved.")
	add_columns()
	# create_table()
	import_data(o.tr_f_csv, o.sd_f_csv, o.lb_f_csv, o.lg_f_csv)
	export_data()
	end = time.time()
	difference = end - start
	b = int((difference - (difference % 60))/60)
	c = '%.2f'%(difference % 60)
	print("\n")
	print("Running CMO Pull...")
	cmoPull.cmoWriteToFile()
	print("Running COR Pull...")
	corPull.corWriteToFile()
	print("\n")
	print("Uploading PORT Data to Servers...")
	today = datetime.date.today()
	security2db.day2db(str(today.day).zfill(2), str(today.month).zfill(2), str(today.year - 2000))
	print("\n")
	print("Time to run mp_driver.py script: ",b,"minutes, ",c,"seconds")
