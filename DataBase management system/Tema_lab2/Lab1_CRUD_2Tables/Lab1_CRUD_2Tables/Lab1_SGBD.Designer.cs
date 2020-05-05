namespace Lab1_CRUD_2Tables
{
    partial class Lab1_SGBD
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
            this.addrGridView = new System.Windows.Forms.DataGridView();
            this.providerGridView = new System.Windows.Forms.DataGridView();
            this.ParentTableLabel = new System.Windows.Forms.Label();
            this.ChildTableLabel = new System.Windows.Forms.Label();
            this.showAdrBtn = new System.Windows.Forms.Button();
            this.nameLbl = new System.Windows.Forms.Label();
            this.quantLbl = new System.Windows.Forms.Label();
            this.providerNameTxt = new System.Windows.Forms.TextBox();
            this.providerQuantityTxt = new System.Windows.Forms.TextBox();
            this.updBtn = new System.Windows.Forms.Button();
            this.delBtn = new System.Windows.Forms.Button();
            this.AddBtn = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.dead_btn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize) (this.addrGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize) (this.providerGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // addrGridView
            // 
            this.addrGridView.ColumnHeadersHeightSizeMode =
                System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.addrGridView.Location = new System.Drawing.Point(33, 140);
            this.addrGridView.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.addrGridView.Name = "addrGridView";
            this.addrGridView.Size = new System.Drawing.Size(641, 812);
            this.addrGridView.TabIndex = 0;
            this.addrGridView.SelectionChanged += new System.EventHandler(this.addrGridView_SelectionChanged);
            // 
            // providerGridView
            // 
            this.providerGridView.ColumnHeadersHeightSizeMode =
                System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.providerGridView.Location = new System.Drawing.Point(829, 140);
            this.providerGridView.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.providerGridView.Name = "providerGridView";
            this.providerGridView.Size = new System.Drawing.Size(680, 812);
            this.providerGridView.TabIndex = 1;
            this.providerGridView.SelectionChanged += new System.EventHandler(this.providerGridView_SelectionChanged);
            // 
            // ParentTableLabel
            // 
            this.ParentTableLabel.AutoSize = true;
            this.ParentTableLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F,
                System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.ParentTableLabel.Location = new System.Drawing.Point(256, 58);
            this.ParentTableLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.ParentTableLabel.Name = "ParentTableLabel";
            this.ParentTableLabel.Size = new System.Drawing.Size(142, 39);
            this.ParentTableLabel.TabIndex = 2;
            this.ParentTableLabel.Text = "Address";
            // 
            // ChildTableLabel
            // 
            this.ChildTableLabel.AutoSize = true;
            this.ChildTableLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F,
                System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.ChildTableLabel.Location = new System.Drawing.Point(1081, 58);
            this.ChildTableLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.ChildTableLabel.Name = "ChildTableLabel";
            this.ChildTableLabel.Size = new System.Drawing.Size(144, 39);
            this.ChildTableLabel.TabIndex = 3;
            this.ChildTableLabel.Text = "Provider";
            // 
            // showAdrBtn
            // 
            this.showAdrBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F,
                System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.showAdrBtn.Location = new System.Drawing.Point(1555, 689);
            this.showAdrBtn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.showAdrBtn.Name = "showAdrBtn";
            this.showAdrBtn.Size = new System.Drawing.Size(204, 58);
            this.showAdrBtn.TabIndex = 4;
            this.showAdrBtn.Text = "Show Addresses";
            this.showAdrBtn.UseVisualStyleBackColor = true;
            this.showAdrBtn.Click += new System.EventHandler(this.showAdrBtn_Click);
            // 
            // nameLbl
            // 
            this.nameLbl.AutoSize = true;
            this.nameLbl.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.nameLbl.Location = new System.Drawing.Point(1568, 546);
            this.nameLbl.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.nameLbl.Name = "nameLbl";
            this.nameLbl.Size = new System.Drawing.Size(63, 20);
            this.nameLbl.TabIndex = 6;
            this.nameLbl.Text = "Name:";
            // 
            // quantLbl
            // 
            this.quantLbl.AutoSize = true;
            this.quantLbl.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.quantLbl.Location = new System.Drawing.Point(1568, 629);
            this.quantLbl.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.quantLbl.Name = "quantLbl";
            this.quantLbl.Size = new System.Drawing.Size(91, 20);
            this.quantLbl.TabIndex = 7;
            this.quantLbl.Text = "Quantity: ";
            // 
            // providerNameTxt
            // 
            this.providerNameTxt.Location = new System.Drawing.Point(1733, 546);
            this.providerNameTxt.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.providerNameTxt.Name = "providerNameTxt";
            this.providerNameTxt.Size = new System.Drawing.Size(180, 27);
            this.providerNameTxt.TabIndex = 8;
            // 
            // providerQuantityTxt
            // 
            this.providerQuantityTxt.Location = new System.Drawing.Point(1733, 622);
            this.providerQuantityTxt.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.providerQuantityTxt.Name = "providerQuantityTxt";
            this.providerQuantityTxt.Size = new System.Drawing.Size(180, 27);
            this.providerQuantityTxt.TabIndex = 9;
            // 
            // updBtn
            // 
            this.updBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.updBtn.Location = new System.Drawing.Point(1780, 861);
            this.updBtn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.updBtn.Name = "updBtn";
            this.updBtn.Size = new System.Drawing.Size(127, 52);
            this.updBtn.TabIndex = 11;
            this.updBtn.Text = "Update";
            this.updBtn.UseVisualStyleBackColor = true;
            this.updBtn.Click += new System.EventHandler(this.providerAddBtn_Click);
            // 
            // delBtn
            // 
            this.delBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.delBtn.Location = new System.Drawing.Point(1780, 689);
            this.delBtn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.delBtn.Name = "delBtn";
            this.delBtn.Size = new System.Drawing.Size(127, 52);
            this.delBtn.TabIndex = 12;
            this.delBtn.Text = "Delete";
            this.delBtn.UseVisualStyleBackColor = true;
            this.delBtn.Click += new System.EventHandler(this.delBtn_Click);
            // 
            // AddBtn
            // 
            this.AddBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.AddBtn.Location = new System.Drawing.Point(1780, 782);
            this.AddBtn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.AddBtn.Name = "AddBtn";
            this.AddBtn.Size = new System.Drawing.Size(127, 52);
            this.AddBtn.TabIndex = 13;
            this.AddBtn.Text = "Add";
            this.AddBtn.UseVisualStyleBackColor = true;
            this.AddBtn.Click += new System.EventHandler(this.AddBtn_Click);
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(1587, 140);
            this.panel1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(320, 380);
            this.panel1.TabIndex = 14;
            // 
            // dead_btn
            // 
            this.dead_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular,
                System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.dead_btn.Location = new System.Drawing.Point(1555, 782);
            this.dead_btn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dead_btn.Name = "dead_btn";
            this.dead_btn.Size = new System.Drawing.Size(204, 58);
            this.dead_btn.TabIndex = 15;
            this.dead_btn.Text = "Deadlock";
            this.dead_btn.UseVisualStyleBackColor = true;
            this.dead_btn.Click += new System.EventHandler(this.dead_btn_Click);
            // 
            // Lab1_SGBD
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1923, 1001);
            this.Controls.Add(this.dead_btn);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.AddBtn);
            this.Controls.Add(this.delBtn);
            this.Controls.Add(this.updBtn);
            this.Controls.Add(this.providerQuantityTxt);
            this.Controls.Add(this.providerNameTxt);
            this.Controls.Add(this.quantLbl);
            this.Controls.Add(this.nameLbl);
            this.Controls.Add(this.showAdrBtn);
            this.Controls.Add(this.ChildTableLabel);
            this.Controls.Add(this.ParentTableLabel);
            this.Controls.Add(this.providerGridView);
            this.Controls.Add(this.addrGridView);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Lab1_SGBD";
            this.Text = "Lab1SGBD";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize) (this.addrGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize) (this.providerGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        #endregion

        private System.Windows.Forms.DataGridView addrGridView;
        private System.Windows.Forms.DataGridView providerGridView;
        private System.Windows.Forms.Label ParentTableLabel;
        private System.Windows.Forms.Label ChildTableLabel;
        private System.Windows.Forms.Button showAdrBtn;
        private System.Windows.Forms.Label nameLbl;
        private System.Windows.Forms.Label quantLbl;
        private System.Windows.Forms.TextBox providerNameTxt;
        private System.Windows.Forms.TextBox providerQuantityTxt;
        private System.Windows.Forms.Button updBtn;
        private System.Windows.Forms.Button delBtn;
        private System.Windows.Forms.Button AddBtn;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button dead_btn;
    }
}

