namespace WindowsFormsApp1
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
            this.childView = new System.Windows.Forms.DataGridView();
            this.parentView = new System.Windows.Forms.DataGridView();
            this.closeButton = new System.Windows.Forms.Button();
            this.updateButton = new System.Windows.Forms.Button();
            this.deleteButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize) (this.childView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize) (this.parentView)).BeginInit();
            this.SuspendLayout();
            // 
            // childView
            // 
            this.childView.AllowUserToOrderColumns = true;
            this.childView.ColumnHeadersHeightSizeMode =
                System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.childView.Location = new System.Drawing.Point(18, 46);
            this.childView.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.childView.Name = "childView";
            this.childView.RowTemplate.Height = 24;
            this.childView.Size = new System.Drawing.Size(644, 492);
            this.childView.TabIndex = 0;
            // 
            // parentView
            // 
            this.parentView.AllowUserToOrderColumns = true;
            this.parentView.ColumnHeadersHeightSizeMode =
                System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.parentView.Location = new System.Drawing.Point(711, 46);
            this.parentView.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.parentView.Name = "parentView";
            this.parentView.RowTemplate.Height = 24;
            this.parentView.Size = new System.Drawing.Size(320, 491);
            this.parentView.TabIndex = 1;
            this.parentView.CellClick +=
                new System.Windows.Forms.DataGridViewCellEventHandler(this.crateView_CellClick);
            // 
            // closeButton
            // 
            this.closeButton.Location = new System.Drawing.Point(1076, 379);
            this.closeButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.closeButton.Name = "closeButton";
            this.closeButton.Size = new System.Drawing.Size(145, 148);
            this.closeButton.TabIndex = 2;
            this.closeButton.Text = "Close";
            this.closeButton.UseVisualStyleBackColor = true;
            this.closeButton.Click += new System.EventHandler(this.closeButton_Click);
            // 
            // updateButton
            // 
            this.updateButton.Location = new System.Drawing.Point(1076, 202);
            this.updateButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.updateButton.Name = "updateButton";
            this.updateButton.Size = new System.Drawing.Size(147, 148);
            this.updateButton.TabIndex = 3;
            this.updateButton.Text = "Update";
            this.updateButton.UseVisualStyleBackColor = true;
            this.updateButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // deleteButton
            // 
            this.deleteButton.Location = new System.Drawing.Point(1076, 48);
            this.deleteButton.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(146, 121);
            this.deleteButton.TabIndex = 4;
            this.deleteButton.Text = "Delete";
            this.deleteButton.UseVisualStyleBackColor = true;
            this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1234, 561);
            this.Controls.Add(this.deleteButton);
            this.Controls.Add(this.updateButton);
            this.Controls.Add(this.closeButton);
            this.Controls.Add(this.parentView);
            this.Controls.Add(this.childView);
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize) (this.childView)).EndInit();
            ((System.ComponentModel.ISupportInitialize) (this.parentView)).EndInit();
            this.ResumeLayout(false);
        }

        #endregion

        private System.Windows.Forms.Button updateButton;
        private System.Windows.Forms.Button closeButton;
        private System.Windows.Forms.DataGridView parentView;
        private System.Windows.Forms.DataGridView childView;
        private System.Windows.Forms.Button deleteButton;
    }
}