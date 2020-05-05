namespace Laborator1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.vinylView = new System.Windows.Forms.DataGridView();
            this.crateView = new System.Windows.Forms.DataGridView();
            this.Vinyl = new System.Windows.Forms.Label();
            this.crateLabel = new System.Windows.Forms.Label();
            this.showCratesButton = new System.Windows.Forms.Button();
            this.vinylLabel = new System.Windows.Forms.Label();
            this.nameLabel = new System.Windows.Forms.Label();
            this.genreLabel = new System.Windows.Forms.Label();
            this.priceLabel = new System.Windows.Forms.Label();
            this.nameTextBox = new System.Windows.Forms.TextBox();
            this.genreTextBox = new System.Windows.Forms.TextBox();
            this.priceTextBox = new System.Windows.Forms.TextBox();
            this.deleteButton = new System.Windows.Forms.Button();
            this.updateButton = new System.Windows.Forms.Button();
            this.addButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.vinylView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.crateView)).BeginInit();
            this.SuspendLayout();
            // 
            // vinylView
            // 
            this.vinylView.BackgroundColor = System.Drawing.Color.DarkSlateGray;
            this.vinylView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.vinylView.Location = new System.Drawing.Point(12, 53);
            this.vinylView.Name = "vinylView";
            this.vinylView.RowHeadersWidth = 51;
            this.vinylView.RowTemplate.Height = 24;
            this.vinylView.Size = new System.Drawing.Size(742, 406);
            this.vinylView.TabIndex = 1;
            // 
            // crateView
            // 
            this.crateView.AllowUserToOrderColumns = true;
            this.crateView.BackgroundColor = System.Drawing.Color.DarkSlateGray;
            this.crateView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.crateView.Location = new System.Drawing.Point(770, 53);
            this.crateView.Name = "crateView";
            this.crateView.RowHeadersWidth = 51;
            this.crateView.RowTemplate.Height = 24;
            this.crateView.Size = new System.Drawing.Size(343, 406);
            this.crateView.TabIndex = 2;
            this.crateView.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.crateView_CellClick);
            // 
            // Vinyl
            // 
            this.Vinyl.AutoSize = true;
            this.Vinyl.Font = new System.Drawing.Font("MV Boli", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Vinyl.Location = new System.Drawing.Point(302, 13);
            this.Vinyl.Name = "Vinyl";
            this.Vinyl.Size = new System.Drawing.Size(84, 37);
            this.Vinyl.TabIndex = 3;
            this.Vinyl.Text = "Vinyl";
            // 
            // crateLabel
            // 
            this.crateLabel.AutoSize = true;
            this.crateLabel.Font = new System.Drawing.Font("MV Boli", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.crateLabel.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.crateLabel.Location = new System.Drawing.Point(893, 13);
            this.crateLabel.Name = "crateLabel";
            this.crateLabel.Size = new System.Drawing.Size(94, 37);
            this.crateLabel.TabIndex = 4;
            this.crateLabel.Text = "Crate";
            // 
            // showCratesButton
            // 
            this.showCratesButton.BackColor = System.Drawing.Color.DarkCyan;
            this.showCratesButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.showCratesButton.Font = new System.Drawing.Font("MV Boli", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.showCratesButton.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.showCratesButton.Location = new System.Drawing.Point(1146, 53);
            this.showCratesButton.Name = "showCratesButton";
            this.showCratesButton.Size = new System.Drawing.Size(343, 51);
            this.showCratesButton.TabIndex = 5;
            this.showCratesButton.Text = "Show Crates";
            this.showCratesButton.UseVisualStyleBackColor = false;
            this.showCratesButton.Click += new System.EventHandler(this.showCratesButton_Click);
            // 
            // vinylLabel
            // 
            this.vinylLabel.AutoSize = true;
            this.vinylLabel.Font = new System.Drawing.Font("MV Boli", 19.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.vinylLabel.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.vinylLabel.Location = new System.Drawing.Point(1270, 107);
            this.vinylLabel.Name = "vinylLabel";
            this.vinylLabel.Size = new System.Drawing.Size(97, 44);
            this.vinylLabel.TabIndex = 7;
            this.vinylLabel.Text = "Vinyl";
            // 
            // nameLabel
            // 
            this.nameLabel.AutoSize = true;
            this.nameLabel.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nameLabel.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.nameLabel.Location = new System.Drawing.Point(1140, 170);
            this.nameLabel.Name = "nameLabel";
            this.nameLabel.Size = new System.Drawing.Size(82, 31);
            this.nameLabel.TabIndex = 8;
            this.nameLabel.Text = "Name";
            // 
            // genreLabel
            // 
            this.genreLabel.AutoSize = true;
            this.genreLabel.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.genreLabel.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.genreLabel.Location = new System.Drawing.Point(1140, 213);
            this.genreLabel.Name = "genreLabel";
            this.genreLabel.Size = new System.Drawing.Size(82, 31);
            this.genreLabel.TabIndex = 9;
            this.genreLabel.Text = "Genre";
            // 
            // priceLabel
            // 
            this.priceLabel.AutoSize = true;
            this.priceLabel.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.priceLabel.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.priceLabel.Location = new System.Drawing.Point(1140, 253);
            this.priceLabel.Name = "priceLabel";
            this.priceLabel.Size = new System.Drawing.Size(73, 31);
            this.priceLabel.TabIndex = 10;
            this.priceLabel.Text = "Price";
            // 
            // nameTextBox
            // 
            this.nameTextBox.Location = new System.Drawing.Point(1229, 179);
            this.nameTextBox.Name = "nameTextBox";
            this.nameTextBox.Size = new System.Drawing.Size(260, 22);
            this.nameTextBox.TabIndex = 11;
            // 
            // genreTextBox
            // 
            this.genreTextBox.Location = new System.Drawing.Point(1229, 220);
            this.genreTextBox.Name = "genreTextBox";
            this.genreTextBox.Size = new System.Drawing.Size(260, 22);
            this.genreTextBox.TabIndex = 12;
            // 
            // priceTextBox
            // 
            this.priceTextBox.Location = new System.Drawing.Point(1229, 260);
            this.priceTextBox.Name = "priceTextBox";
            this.priceTextBox.Size = new System.Drawing.Size(260, 22);
            this.priceTextBox.TabIndex = 13;
            // 
            // deleteButton
            // 
            this.deleteButton.BackColor = System.Drawing.Color.DarkCyan;
            this.deleteButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.deleteButton.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.deleteButton.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.deleteButton.Location = new System.Drawing.Point(1146, 347);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(141, 53);
            this.deleteButton.TabIndex = 14;
            this.deleteButton.Text = "Delete";
            this.deleteButton.UseVisualStyleBackColor = false;
            this.deleteButton.Click += new System.EventHandler(this.delButton_Click);
            // 
            // updateButton
            // 
            this.updateButton.BackColor = System.Drawing.Color.DarkCyan;
            this.updateButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.updateButton.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.updateButton.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.updateButton.Location = new System.Drawing.Point(1339, 347);
            this.updateButton.Name = "updateButton";
            this.updateButton.Size = new System.Drawing.Size(150, 53);
            this.updateButton.TabIndex = 15;
            this.updateButton.Text = "Update";
            this.updateButton.UseVisualStyleBackColor = false;
            this.updateButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // addButton
            // 
            this.addButton.BackColor = System.Drawing.Color.DarkCyan;
            this.addButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.addButton.Font = new System.Drawing.Font("MV Boli", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.addButton.ForeColor = System.Drawing.Color.MediumSeaGreen;
            this.addButton.Location = new System.Drawing.Point(1229, 432);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(201, 64);
            this.addButton.TabIndex = 16;
            this.addButton.Text = "Add";
            this.addButton.UseVisualStyleBackColor = false;
            this.addButton.Click += new System.EventHandler(this.addVinylButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.SeaGreen;
            this.ClientSize = new System.Drawing.Size(1549, 532);
            this.Controls.Add(this.addButton);
            this.Controls.Add(this.updateButton);
            this.Controls.Add(this.deleteButton);
            this.Controls.Add(this.priceTextBox);
            this.Controls.Add(this.genreTextBox);
            this.Controls.Add(this.nameTextBox);
            this.Controls.Add(this.priceLabel);
            this.Controls.Add(this.genreLabel);
            this.Controls.Add(this.nameLabel);
            this.Controls.Add(this.vinylLabel);
            this.Controls.Add(this.showCratesButton);
            this.Controls.Add(this.Vinyl);
            this.Controls.Add(this.crateLabel);
            this.Controls.Add(this.crateView);
            this.Controls.Add(this.vinylView);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.vinylView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.crateView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.DataGridView vinylView;
        private System.Windows.Forms.DataGridView crateView;
        private System.Windows.Forms.Label Vinyl;
        private System.Windows.Forms.Label crateLabel;
        private System.Windows.Forms.Button showCratesButton;
        private System.Windows.Forms.Label vinylLabel;
        private System.Windows.Forms.Label nameLabel;
        private System.Windows.Forms.Label genreLabel;
        private System.Windows.Forms.Label priceLabel;
        private System.Windows.Forms.TextBox nameTextBox;
        private System.Windows.Forms.TextBox genreTextBox;
        private System.Windows.Forms.TextBox priceTextBox;
        private System.Windows.Forms.Button deleteButton;
        private System.Windows.Forms.Button updateButton;
        private System.Windows.Forms.Button addButton;
    }
}

