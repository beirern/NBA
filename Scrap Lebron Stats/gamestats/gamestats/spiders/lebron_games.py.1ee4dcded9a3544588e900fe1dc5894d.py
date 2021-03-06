import scrapy
import pandas as pd
import numpy as np


class GameSpider(scrapy.Spider):
    # Scrapy Variables
    name = "Lebron"

    # TODO: PUT ALL URLS (END OF URL CHANGES BY 100 EACH TIME) DO NOT DO THE FOLLOW PAGE METHOD
    start_urls = [
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=100",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=200",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=300",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=400",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=500",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=600",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=700",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=800",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=900",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=1000",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=1100",
        "https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=jamesle01&match=game&year_min=1947&year_max=2020&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=1&game_num_max=1&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset=1200",
    ]

    # Variables for table
    headers = []
    stats = [[]]

    def parse(self, response):
        # Get Headers and different parts of table
        table = response.css("div#div_stats")
        self.headers = table.css("thead th::text")[1:].getall()
        data_numbers = table.css("tbody tr td::text").getall()
        data_misc = table.css("tbody tr td a::text").getall()

        # Math stuff for figuring out indicies
        row_length = len(self.headers)
        num_rows = int(len(data_numbers) / 27)
        # stats = np.empty([num_rows, len(headers)], dtype=object)
        misc_indicies = [1, 2, 4]

        # Add in blank data for header
        self.headers[3] = "Home"
        self.headers[5] = "Win"

        # Add in where there should be blank data for numbers
        row_length_num = row_length - 3
        field_goals = [5, 8, 11, 14]
        for i in range(len(data_numbers)):
            # Blank for no @ in Away or Home
            if i % row_length_num == 1:
                if data_numbers[i] == "@":
                    data_numbers[i] = "A"
                else:
                    data_numbers.insert(i, "H")
            # FG and FGA
            elif i % row_length_num in field_goals:
                if data_numbers[i] == "0" and data_numbers[i + 1] == "0":
                    data_numbers.insert(i + 2, "")

        # Add all the numbers and misc parts of table to a list
        for i in range(num_rows):
            row_data = []
            for j in range(row_length):
                if j % row_length in misc_indicies:
                    row_data.append(data_misc[0])
                    data_misc.pop(0)
                else:
                    row_data.append(data_numbers[0])
                    data_numbers.pop(0)
            self.stats.append(row_data)

        if response.url.split("=")[-1] == "1200":  # If there is another page of data
            # Convert to numpy array and use pandas
            self.stats.pop(0)
            self.stats = np.array(self.stats)
            stats_table = pd.DataFrame(self.stats, columns=self.headers)
            stats_table.to_csv(r".\lebron_games.csv", index=None, header=True)
